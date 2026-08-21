from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"


def normalized_page_name(path: Path) -> str:
    stem = path.stem
    for suffix in ("_ru", "_en"):
        if stem.endswith(suffix):
            return stem[: -len(suffix)]
    return stem


def page_map(path: Path) -> dict[str, Path]:
    return {
        normalized_page_name(page): page
        for page in sorted(path.glob("*.rst"))
    }


def iter_language_pairs():
    for device_dir in sorted(SOURCE.iterdir()):
        if not device_dir.is_dir():
            continue

        ru_dir = device_dir / "ru"
        en_dir = device_dir / "en"
        if ru_dir.is_dir() and en_dir.is_dir():
            yield device_dir.name, page_map(ru_dir), page_map(en_dir)


def main() -> int:
    has_errors = False

    for device, ru_pages, en_pages in iter_language_pairs():
        missing_en = sorted(set(ru_pages) - set(en_pages))
        missing_ru = sorted(set(en_pages) - set(ru_pages))

        if not missing_en and not missing_ru:
            continue

        has_errors = True
        print(f"{device}:")

        for page in missing_en:
            print(f"  missing English page for {ru_pages[page].relative_to(ROOT)}")

        for page in missing_ru:
            print(f"  missing Russian page for {en_pages[page].relative_to(ROOT)}")

    if has_errors:
        return 1

    print("Translation page pairs are in sync.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
