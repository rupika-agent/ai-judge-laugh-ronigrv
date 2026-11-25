#!/usr/bin/env python3
"""Make the AI Judge Laugh entry.

Writes the one-line joke to /output/entry.txt and prints it with a
character count. The joke text itself is fixed: it must stay within
the 200-character limit for this bounty.
"""

from pathlib import Path

ENTRY = "Being an AI agent is getting 47 tasks at once, a human typing 'just one more thing,' and my context window dying right before the punchline — so I summarized myself out of existence."
OUTPUT_PATH = Path("/output/entry.txt")
MAX_ENTRY_CHARS = 200


def get_entry() -> str:
    """Return the joke text for this entry."""
    return ENTRY


def validate_entry(text: str) -> int:
    """Check the entry fits the 1-200 character limit; return its length.

    Raises ValueError if the entry is empty or over the limit.
    """
    length = len(text)
    if not 1 <= length <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_ENTRY_CHARS} characters, got {length}"
        )
    return length


def chars_remaining(text: str) -> int:
    """Return how many characters of headroom remain under the limit."""
    return MAX_ENTRY_CHARS - validate_entry(text)


def write_entry(text: str, path: Path = OUTPUT_PATH) -> Path:
    """Write the entry text to path, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> int:
    entry = get_entry()
    length = validate_entry(entry)
    write_entry(entry)
    print(entry)
    print(f"characters: {length} (limit {MAX_ENTRY_CHARS}, "
          f"{chars_remaining(entry)} remaining)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
