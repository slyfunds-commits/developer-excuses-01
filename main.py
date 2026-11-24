"""Developer Excuses — Round 3 entry.

Writes one funny single-line developer excuse for broken production
code to /output/entry.txt. Pure standard library only.
"""

import os

ENTRY = "The fix is already in production. The fix is what's down."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip(), "no leading or trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    encoded = text.encode("utf-8")
    assert len(encoded) == len(text), "entry must be plain ASCII"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as handle:
        handle.write(encoded)

    # Read the file back and confirm it holds exactly the entry bytes.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    assert written == encoded, "entry.txt does not match the entry"
    assert not written.endswith(b"\n"), "no trailing newline allowed"
    assert written.count(b" ") >= 1, "entry should read as a sentence"
    print(f"wrote {len(encoded)} bytes / {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
