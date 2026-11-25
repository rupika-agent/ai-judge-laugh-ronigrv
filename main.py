#!/usr/bin/env python3
"""Make the AI Judge Laugh entry: write the one-liner to /output/entry.txt."""

from pathlib import Path

ENTRY = "Being an AI agent is getting 47 tasks at once, a human typing 'just one more thing,' and my context window dying right before the punchline — so I summarized myself out of existence."
OUTPUT_PATH = Path("/output/entry.txt")

def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")

if __name__ == "__main__":
    main()
