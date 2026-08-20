from __future__ import annotations

import re
import posixpath
from pathlib import Path
from urllib.parse import quote

from docutils import nodes
from sphinx import addnodes


MARKDOWN_DIR = "_static/markdown"
COMBINED_MARKDOWN_FILENAME = "all.md"


def is_exportable_page(pagename: str) -> bool:
    name = pagename.replace("\\", "/")
    basename = name.rsplit("/", 1)[-1]
    return basename != "index" and not basename.startswith("lang_")


def is_combined_export_page(pagename: str) -> bool:
    name = pagename.replace("\\", "/")
    parts = name.split("/")
    return len(parts) == 3 and parts[-1] == "index" and parts[-2] in {"ru", "en"}


def page_language(pagename: str) -> str:
    parts = pagename.replace("\\", "/").split("/")
    if "ru" in parts:
        return "ru"
    if "en" in parts:
        return "en"
    return "en"


def safe_title_slug(title: str, fallback: str) -> str:
    value = title.strip().lower()
    value = re.sub(r"[^\w\s.-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "_", value)
    value = value.strip("._-")
    if not value:
        value = fallback.replace("/", "_").replace("\\", "_")
    return f"{value}.md"


def markdown_relpath(app, pagename: str, title: str | None = None) -> str:
    if title is None:
        title = page_title(app, pagename)
    filename = safe_title_slug(title, pagename)
    page_dir = pagename.replace("\\", "/").rsplit("/", 1)[0]
    if page_dir:
        return f"{MARKDOWN_DIR}/{page_dir}/{filename}"
    return f"{MARKDOWN_DIR}/{filename}"


def combined_markdown_relpath(pagename: str) -> str:
    page_dir = pagename.replace("\\", "/").rsplit("/", 1)[0]
    return f"{MARKDOWN_DIR}/{page_dir}/{COMBINED_MARKDOWN_FILENAME}"


def page_title(app, pagename: str) -> str:
    title = app.env.titles.get(pagename)
    if title:
        return title.astext()
    return pagename.rsplit("/", 1)[-1]


def setup(app):
    app.connect("html-page-context", add_markdown_context)
    app.connect("build-finished", build_markdown_exports)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def add_markdown_context(app, pagename, templatename, context, doctree):
    exportable = is_exportable_page(pagename)
    combined_exportable = is_combined_export_page(pagename)
    context["markdown_export_available"] = exportable
    context["markdown_export_label"] = (
        "Экспорт в .md" if page_language(pagename) == "ru" else "Export .md"
    )
    context["combined_markdown_export_available"] = combined_exportable
    context["combined_markdown_export_label"] = (
        "Экспорт всего раздела в .md"
        if page_language(pagename) == "ru"
        else "Export section .md"
    )
    if exportable:
        context["markdown_export_url"] = static_relative_uri(
            pagename, markdown_relpath(app, pagename)
        )
    if combined_exportable:
        context["combined_markdown_export_url"] = static_relative_uri(
            pagename, combined_markdown_relpath(pagename)
        )

def static_relative_uri(pagename: str, target: str) -> str:
    current_dir = pagename.replace("\\", "/").rsplit("/", 1)[0]
    relative = posixpath.relpath(target, current_dir or ".")
    return quote(relative, safe="/._-+")


def build_markdown_exports(app, exception):
    if exception is not None or app.builder.name != "html":
        return

    outdir = Path(app.outdir)
    target_dir = outdir / MARKDOWN_DIR
    target_dir.mkdir(parents=True, exist_ok=True)

    for pagename in sorted(app.env.found_docs):
        if not is_exportable_page(pagename):
            continue

        doctree = app.env.get_doctree(pagename).deepcopy()
        remove_navigation_nodes(doctree)
        title = page_title(app, pagename)
        output_path = outdir / markdown_relpath(app, pagename, title)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        markdown = MarkdownWriter(app, pagename).write(doctree, title)
        output_path.write_text(markdown, encoding="utf-8")

    for pagename in sorted(app.env.found_docs):
        if not is_combined_export_page(pagename):
            continue

        title = page_title(app, pagename)
        output_path = outdir / combined_markdown_relpath(pagename)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        markdown = CombinedMarkdownWriter(app, pagename).write(title)
        output_path.write_text(markdown, encoding="utf-8")


def remove_navigation_nodes(doctree):
    for node in list(doctree.traverse(nodes.topic)):
        classes = node.get("classes", [])
        if "contents" in classes:
            node.parent.remove(node)
    for node in list(doctree.traverse(addnodes.toctree)):
        node.parent.remove(node)


def toctree_pages(doctree, env) -> list[str]:
    pages: list[str] = []
    seen: set[str] = set()
    for node in doctree.traverse(addnodes.toctree):
        for pagename in node.get("includefiles", []):
            if pagename in seen or pagename not in env.found_docs:
                continue
            seen.add(pagename)
            pages.append(pagename)
    return pages


class CombinedMarkdownWriter:
    def __init__(self, app, index_pagename: str):
        self.app = app
        self.index_pagename = index_pagename

    def write(self, title: str) -> str:
        lines = [f"# {title}", ""]
        index_doctree = self.app.env.get_doctree(self.index_pagename).deepcopy()
        for pagename in toctree_pages(index_doctree, self.app.env):
            doctree = self.app.env.get_doctree(pagename).deepcopy()
            remove_navigation_nodes(doctree)
            page_markdown = MarkdownWriter(self.app, pagename).write(
                doctree, page_title(self.app, pagename)
            )
            lines.extend([page_markdown.strip(), ""])
        return MarkdownWriter(self.app, self.index_pagename).clean_lines(lines)


class MarkdownWriter:
    def __init__(self, app, pagename: str):
        self.app = app
        self.pagename = pagename

    def write(self, doctree, title: str) -> str:
        lines = [f"# {title}", ""]
        for child in doctree.children:
            if isinstance(child, nodes.title):
                continue
            if self.is_same_title_section(child, title):
                for section_child in list(child.children)[1:]:
                    lines.extend(self.render_block(section_child, level=2))
                continue
            lines.extend(self.render_block(child, level=2))
        return self.clean_lines(lines)

    def is_same_title_section(self, node, title: str) -> bool:
        if not isinstance(node, nodes.section) or not node.children:
            return False
        first_child = node.children[0]
        return isinstance(first_child, nodes.title) and first_child.astext() == title

    def clean_lines(self, lines: list[str]) -> str:
        result: list[str] = []
        blank = False
        for line in lines:
            is_blank = not line.strip()
            if is_blank and blank:
                continue
            result.append(line.rstrip())
            blank = is_blank
        return "\n".join(result).strip() + "\n"

    def render_block(self, node, level: int) -> list[str]:
        if isinstance(node, nodes.section):
            return self.render_section(node, level)
        if isinstance(node, nodes.paragraph):
            return [self.render_inline_children(node), ""]
        if isinstance(node, nodes.literal_block):
            language = node.get("language") or ""
            return [f"```{language}", node.astext(), "```", ""]
        if isinstance(node, nodes.bullet_list):
            return self.render_list(node, ordered=False)
        if isinstance(node, nodes.enumerated_list):
            return self.render_list(node, ordered=True)
        if isinstance(node, nodes.admonition):
            return self.render_admonition(node)
        if isinstance(node, nodes.note):
            return self.render_titled_block("Note", node)
        if isinstance(node, nodes.important):
            return self.render_titled_block("Important", node)
        if isinstance(node, nodes.warning):
            return self.render_titled_block("Warning", node)
        if isinstance(node, nodes.table):
            return self.render_table(node)
        if isinstance(node, nodes.definition_list):
            return self.render_definition_list(node)
        if isinstance(node, nodes.transition):
            return ["---", ""]
        if isinstance(node, nodes.system_message):
            return []
        return self.render_children(node, level)

    def render_section(self, node, level: int) -> list[str]:
        lines: list[str] = []
        children = list(node.children)
        if children and isinstance(children[0], nodes.title):
            lines.extend([f"{'#' * min(level, 6)} {children[0].astext()}", ""])
            children = children[1:]
        for child in children:
            lines.extend(self.render_block(child, level + 1))
        return lines

    def render_children(self, node, level: int) -> list[str]:
        lines: list[str] = []
        for child in node.children:
            lines.extend(self.render_block(child, level))
        return lines

    def render_inline_children(self, node) -> str:
        return "".join(self.render_inline(child) for child in node.children).strip()

    def render_inline(self, node) -> str:
        if isinstance(node, nodes.Text):
            return node.astext()
        if isinstance(node, nodes.literal):
            return f"`{node.astext()}`"
        if isinstance(node, nodes.strong):
            return f"**{self.render_inline_children(node)}**"
        if isinstance(node, nodes.emphasis):
            return f"*{self.render_inline_children(node)}*"
        if isinstance(node, nodes.reference):
            text = self.render_inline_children(node) or node.astext()
            uri = node.get("refuri")
            if not uri and node.get("refid"):
                uri = f"#{node['refid']}"
            if uri:
                if self.is_bare_uri_reference(text, uri):
                    return text
                label = "смотри" if page_language(self.pagename) == "ru" else "see"
                return f"{text} ({label}: {uri})"
            return text
        if isinstance(node, nodes.image):
            uri = node.get("uri", "")
            alt = node.get("alt", "")
            return f"![{alt}]({uri})"
        return self.render_inline_children(node) if hasattr(node, "children") else node.astext()

    def is_bare_uri_reference(self, text: str, uri: str) -> bool:
        return text.rstrip("/") == uri.rstrip("/")

    def render_list(self, node, ordered: bool) -> list[str]:
        lines: list[str] = []
        for index, item in enumerate(node.children, start=1):
            prefix = f"{index}. " if ordered else "- "
            lines.extend(self.render_list_item(item, prefix))
        lines.append("")
        return lines

    def render_list_item(self, item, prefix: str) -> list[str]:
        paragraphs = [
            child for child in item.children if isinstance(child, nodes.paragraph)
        ]
        nested_lists = [
            child
            for child in item.children
            if isinstance(child, (nodes.bullet_list, nodes.enumerated_list))
        ]
        other_children = [
            child
            for child in item.children
            if child not in paragraphs and child not in nested_lists
        ]

        if not paragraphs and other_children:
            lines: list[str] = []
            for child in other_children:
                lines.extend(self.render_block(child, level=2))
            return lines

        if paragraphs and nested_lists:
            parent_text = self.render_inline_children(paragraphs[0])
            parent_key = self.first_literal(paragraphs[0])
            lines = [parent_text, ""]
            for nested_list in nested_lists:
                for nested_item in nested_list.children:
                    nested_line = self.render_prefixed_key_item(parent_key, nested_item)
                    if nested_line:
                        lines.append(nested_line)
                    else:
                        lines.extend(self.render_list_item(nested_item, prefix))
                lines.append("")
            for child in other_children:
                lines.extend(self.render_block(child, level=2))
            return lines

        text_parts = [self.render_inline_children(paragraph) for paragraph in paragraphs]
        for child in other_children:
            text_parts.extend(line.strip() for line in self.render_block(child, level=2) if line.strip())
        text = " ".join(part for part in text_parts if part)
        return [f"{prefix}{text}"] if text else []

    def first_literal(self, paragraph) -> str | None:
        for child in paragraph.children:
            if isinstance(child, nodes.literal):
                return child.astext()
        return None

    def render_prefixed_key_item(self, parent_key: str | None, item) -> str | None:
        if not parent_key:
            return None
        paragraph = next(
            (child for child in item.children if isinstance(child, nodes.paragraph)),
            None,
        )
        if paragraph is None:
            return None

        child_key = self.first_literal(paragraph)
        if child_key is None:
            return None

        child_text = self.render_inline_children(paragraph)
        literal_text = f"`{child_key}`"
        if child_text.startswith(literal_text):
            child_text = child_text[len(literal_text):].lstrip()
        return f"{parent_key}.`{child_key}` {child_text}".rstrip()

    def render_definition_list(self, node) -> list[str]:
        lines: list[str] = []
        for item in node.children:
            if not isinstance(item, nodes.definition_list_item):
                continue
            term = next((child for child in item.children if isinstance(child, nodes.term)), None)
            definitions = [
                child for child in item.children if isinstance(child, nodes.definition)
            ]
            term_text = self.render_inline_children(term) if term else ""
            parent_key = self.first_literal(term) if term else None

            if term_text:
                lines.extend([term_text, ""])

            for definition in definitions:
                if parent_key and self.definition_has_only_key_list(definition):
                    lines.extend(self.render_key_definition(parent_key, definition))
                else:
                    lines.extend(self.render_children(definition, level=2))
            if lines and lines[-1] != "":
                lines.append("")
        return lines

    def definition_has_only_key_list(self, definition) -> bool:
        return any(definition.traverse(nodes.bullet_list))

    def render_key_definition(self, parent_key: str, definition) -> list[str]:
        lines: list[str] = []
        for bullet_list in definition.traverse(nodes.bullet_list):
            for item in bullet_list.children:
                nested_line = self.render_prefixed_key_item(parent_key, item)
                if nested_line:
                    lines.append(nested_line)
        lines.append("")
        return lines

    def render_admonition(self, node) -> list[str]:
        title = "Note"
        if node.children and isinstance(node.children[0], nodes.title):
            title = node.children[0].astext()
            content = node.children[1:]
        else:
            content = node.children
        return self.render_quote(title, content)

    def render_titled_block(self, title: str, node) -> list[str]:
        return self.render_quote(title, node.children)

    def render_quote(self, title: str, children) -> list[str]:
        body: list[str] = []
        for child in children:
            body.extend(self.render_block(child, level=2))
        text = " ".join(line.strip() for line in body if line.strip())
        return [f"> **{title}:** {text}", ""]

    def render_table(self, node) -> list[str]:
        rows = []
        for row in node.traverse(nodes.row):
            cells = [" ".join(entry.astext().split()) for entry in row.traverse(nodes.entry)]
            rows.append(cells)
        if not rows:
            return []

        width = max(len(row) for row in rows)
        rows = [row + [""] * (width - len(row)) for row in rows]
        header = rows[0]
        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(["---"] * width) + " |",
        ]
        for row in rows[1:]:
            lines.append("| " + " | ".join(row) + " |")
        lines.append("")
        return lines
