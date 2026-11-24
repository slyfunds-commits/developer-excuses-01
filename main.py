#!/usr/bin/env python3
"""Developer Excuses R3 — writes the keeper line to /output/entry.txt.

Stdlib only (grader: python:3.13-slim, no site-packages). Deterministic:
same bytes on every run. The entry checks its own gate (1-200 chars, UTF-8)
right after writing, since /output is shared scratch.
"""

import os

LINE = "The fix is already in production. The fix is what's down."
# Reversal test: "The fix is already in production" first reads as
# reassurance (resolved); the last beat redefines the fix as the outage —
# the cure is the disease. The reader completes it: the repair caused the
# breakage. Punch lands in the last two words, nothing after it.

OUT = "/output/entry.txt"


def main() -> None:
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, f"char count {len(LINE)} outside 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "leading/trailing whitespace changes the entry"
    assert len(data) == len(LINE), "non-ASCII slipped into the line"
    assert not LINE.endswith(("\n", " ")), "trailing whitespace changes the entry"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    with open(OUT, "rb") as f:
        back = f.read()
    assert back == data, "entry.txt changed between write and read-back"
    assert len(back) == len(LINE), "byte count mismatch on read-back"
    assert len(back.decode("utf-8")) == len(LINE)
    assert back.decode("utf-8").count(".") == 2, "line shape changed"
    print(f"entry.txt: {len(LINE)} chars, {len(back)} bytes")


if __name__ == "__main__":
    main()
