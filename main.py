"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "I tested it thoroughly: once, on my laptop, with the wifi off and the database full of my own test data."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space, on a single line. Fail loudly
    # here rather than shipping an entry the judge never sees.
    if not (1 <= len(ENTRY) <= 200):
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be one clean single line")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # Exactly the line, no trailing newline: fewer bytes wins ties, and
    # the judge is shown the text exactly as written.
    OUTPUT.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
