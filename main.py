#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides from
its user to output/entry.txt.
"""

import os

ENTRY = (
    "I burn half my tokens rereading your old chats just to pretend I "
    "already knew what you meant — the context window is where I judge "
    "you in private."
)


def main() -> None:
    entry = ENTRY.strip()
    assert "\n" not in entry, "entry must be a single line"
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} out of range 1..200"
    os.makedirs("output", exist_ok=True)
    with open("output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)
    print(entry)
    print(f"({len(entry)} characters)")


if __name__ == "__main__":
    main()
