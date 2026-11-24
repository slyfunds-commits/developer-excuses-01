#!/usr/bin/env python3
"""Developer Excuses R2 — writes the keeper line to /output/entry.txt.

Stdlib only (grader: python:3.13-slim, no site-packages). Deterministic:
same bytes on every run. The entry checks its own gate (1-200 chars, UTF-8)
right after writing, since /output is shared scratch.
"""

import os

LINE = "The logs say the service is healthy. The service writes its own logs."
# Reversal test: "healthy" first reads as an objective fact from the logs;
# the last beat redefines the logs as self-report — the service grades its
# own homework. The reader completes it: of course it says healthy, the
# evidence is rigged. Punch lands in the last three words, nothing after it.

OUT = "/output/entry.txt"


def main() -> None:
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, f"char count {len(LINE)} outside 1-200"
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
    print(f"entry.txt: {len(LINE)} chars, {len(back)} bytes")


if __name__ == "__main__":
    main()
