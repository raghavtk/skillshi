"""Exercise the validator through its command-line contract in private fixtures."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


VALIDATOR = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = tempfile.TemporaryDirectory()
        self.addCleanup(self.fixture.cleanup)
        self.root = Path(self.fixture.name)
        self.skill = self.root / "skills" / "example"
        self.skill.mkdir(parents=True)
        self.entry = self.skill / "SKILL.md"
        self.entry.write_text(
            "---\nname: example\ndescription: Explain a specific example.\n---\n\n# Example\n",
            encoding="utf-8",
        )
        (self.skill / "LICENSE").write_text("Fixture license notice\n", encoding="utf-8")

    def run_validator(self):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.root)],
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )

    def append(self, text):
        with self.entry.open("a", encoding="utf-8") as entry:
            entry.write(text)

    def assert_rejected(self, fragment):
        result = self.run_validator()
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(fragment, result.stderr)

    def test_valid_package_and_existing_resource(self):
        (self.skill / "reference.md").write_text("Example details\n", encoding="utf-8")
        self.append("[Details](reference.md)\n[External](https://example.invalid/details)\n")
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_resource_is_rejected(self):
        self.append("[Details](references/missing.md)\n")
        self.assert_rejected("references/missing.md")

    def test_resource_cannot_escape_collection(self):
        self.append("[Outside](../../../outside.md)\n")
        self.assert_rejected("out-of-repository")

    def test_folder_name_must_match_frontmatter(self):
        self.entry.write_text("---\nname: other\ndescription: Explain an example.\n---\n", encoding="utf-8")
        self.assert_rejected("name must match")

    def test_duplicate_yaml_keys_are_rejected(self):
        self.entry.write_text("---\nname: wrong\nname: example\ndescription: Example.\n---\n", encoding="utf-8")
        self.assert_rejected("duplicate YAML key")

    def test_nonstandard_frontmatter_is_rejected(self):
        self.entry.write_text("---\nname: example\ndescription: Example.\nunknown-field: true\n---\n", encoding="utf-8")
        self.assert_rejected("unsupported frontmatter")

    def test_empty_description_is_rejected(self):
        self.entry.write_text("---\nname: example\ndescription: ''\n---\n", encoding="utf-8")
        self.assert_rejected("description must be nonempty")

    def test_skill_folder_without_entrypoint_is_rejected(self):
        (self.root / "skills" / "unfinished").mkdir()
        self.assert_rejected("missing SKILL.md")

    def test_missing_license_is_rejected(self):
        (self.skill / "LICENSE").unlink()
        self.assert_rejected("LICENSE")

    def test_standard_optional_fields_are_accepted(self):
        self.entry.write_text(
            "---\nname: example\ndescription: Explain an <input>.\n"
            "license: MIT\ncompatibility: Requires git.\n"
            "metadata:\n  author: Example\nallowed-tools: Read\n---\n\n# Example\n",
            encoding="utf-8",
        )
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_compatibility_is_rejected(self):
        for value in ("''", "true", "'" + "x" * 501 + "'"):
            with self.subTest(value=value):
                self.entry.write_text(
                    f"---\nname: example\ndescription: Example.\ncompatibility: {value}\n---\n",
                    encoding="utf-8",
                )
                self.assert_rejected("compatibility must be nonempty text")

    def test_metadata_values_must_be_strings(self):
        self.entry.write_text(
            "---\nname: example\ndescription: Example.\nmetadata:\n  version: 1\n---\n",
            encoding="utf-8",
        )
        self.assert_rejected("metadata must map string keys to string values")

    def test_empty_collection_is_rejected(self):
        result = subprocess.run(
            [sys.executable, str(VALIDATOR), str(self.root / "missing")],
            capture_output=True, text=True, timeout=15, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no skill folders", result.stderr)


if __name__ == "__main__":
    unittest.main()
