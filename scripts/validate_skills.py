"""Validate the collection's packaging contract, without network access."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently accepting the last value."""


def unique_mapping(loader, node):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node)
    return mapping


UniqueLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)


def validate(root):
    root = Path(root).resolve()
    errors = []

    def fail(path, message):
        errors.append(f"{path.relative_to(root)}: {message}")

    def read_yaml(path, content):
        try:
            result = yaml.load(content, Loader=UniqueLoader)
            if not isinstance(result, dict):
                raise ValueError("expected a YAML mapping")
            return result
        except (yaml.YAMLError, ValueError, TypeError) as exc:
            fail(path, f"invalid YAML: {exc}")
            return {}

    skills = sorted(p for p in (root / "skills").glob("*") if p.is_dir())
    if not skills:
        errors.append("skills/: no skill folders found")

    for skill in skills:
        entry = skill / "SKILL.md"
        if not entry.is_file():
            fail(skill, "missing SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            fail(entry, "missing or malformed YAML frontmatter")
            continue
        data = read_yaml(entry, match.group(1))
        name = data.get("name")
        if (
            not isinstance(name, str)
            or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
            or len(name) > 64
            or name != skill.name
        ):
            fail(entry, "name must match its folder and use lowercase hyphenated words")
        description = data.get("description")
        if (
            not isinstance(description, str)
            or not description.strip()
            or len(description) > 1024
        ):
            fail(entry, "description must be nonempty text, at most 1024 characters")
        allowed = {"name", "description", "license", "compatibility", "allowed-tools", "metadata"}
        if set(data) - allowed:
            fail(entry, "unsupported frontmatter fields: " + ", ".join(map(str, set(data) - allowed)))
        if "[TODO:" in text:
            fail(entry, "unfinished skill-creator placeholder")
        license_path = skill / "LICENSE"
        if not license_path.is_file() or not license_path.read_text(encoding="utf-8").strip():
            fail(skill, "missing or empty LICENSE notice")

        if "compatibility" in data:
            compatibility = data["compatibility"]
            if not isinstance(compatibility, str) or not compatibility.strip() or len(compatibility) > 500:
                fail(entry, "compatibility must be nonempty text, at most 500 characters")
        if "metadata" in data:
            metadata = data["metadata"]
            if not isinstance(metadata, dict) or any(
                not isinstance(key, str) or not isinstance(value, str)
                for key, value in metadata.items()
            ):
                fail(entry, "metadata must map string keys to string values")

    # Inline Markdown links used by this collection; fenced examples are excluded.
    # This deliberately does not claim to be a general Markdown parser.
    markdown = list((root / "skills").rglob("*.md")) + list(root.glob("*.md"))
    for path in markdown:
        text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", "", path.read_text(encoding="utf-8"))
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            target = target.strip().strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            linked = (path.parent / unquote(url.path)).resolve()
            if not linked.is_relative_to(root) or not linked.exists():
                fail(path, f"missing or out-of-repository relative link: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        errors = validate(args.root)
    except (OSError, UnicodeError) as exc:
        print(f"Cannot read collection: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(list((args.root / 'skills').glob('*/SKILL.md')))} skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
