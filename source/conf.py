# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Welrok'
copyright = '2025, Welrok'
author = 'Welrok'
release = ''
html_title = 'Welrok Local API'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath('_ext'))

extensions = [
    'myst_parser',
    'markdown_export',
    'sphinx_markdown_builder'
]

# Настройка для поддержки файлов .md на входе (если пишете документацию в MD)
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_extra_path = ['favicon.svg']
html_favicon = 'favicon.svg'
html_css_files = ['language-switch.css']
html_add_permalinks = ""
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/markdown_export.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}


SOURCE_DIR = Path(__file__).resolve().parent


def language_switch(pagename):
    """Return the sibling language page for the current document."""
    if pagename == "index":
        return {"label": "English version", "target": "index_en"}
    if pagename == "index_en":
        return {"label": "Русская версия", "target": "index"}

    if "/ru/" in pagename:
        target = pagename.replace("/ru/", "/en/", 1)
        candidates = []
        if target.endswith("_ru"):
            base = target[:-3]
            candidates.extend([base, f"{base}_en"])
        else:
            candidates.append(target)
        label = "English version"
    elif "/en/" in pagename:
        target = pagename.replace("/en/", "/ru/", 1)
        candidates = []
        if target.endswith("_en"):
            base = target[:-3]
            candidates.extend([f"{base}_ru", base])
        else:
            candidates.extend([f"{target}_ru", target])
        label = "Русская версия"
    else:
        return None

    for candidate in candidates:
        if (SOURCE_DIR / f"{candidate}.rst").exists():
            return {"label": label, "target": candidate}

    return None


def add_language_switch(app, pagename, templatename, context, doctree):
    context["language_switch"] = language_switch(pagename)
    context["current_language"] = "en" if pagename == "index_en" or "/en/" in pagename else "ru"


def setup(app):
    app.connect("html-page-context", add_language_switch)
