#!/usr/bin/env python3
"""Developer Excuses R1 — writes the keeper line to /output/entry.txt.

Stdlib only (grader: python:3.13-slim, no site-packages). Deterministic:
same bytes on every run. The entry asserts its own gate (1-200 chars, UTF-8)
immediately after writing, since /output is shared scratch.
"""

import os

LINE = "The deploy passed all 400 tests. The 401st test is the customer."
# Reversal test: "passed all 400 tests" first reads as proof the deploy was
# safe; the last beat redefines those tests as incomplete and names the
# customer as the real test. The reader completes it — the deploy was never
# truly tested. 401 quietly echoes HTTP 401 for devs; never explained.

OUT = "/output/entry.txt"


def main() -> None:
    data = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, f"char count {len(LINE)} outside 1-200"
    os.makedirs("/output", exist_ok=True)
    with open(OUT, "wb") as f:
        f.write(data)
    # Verify immediately after writing (shared scratch: read back what we wrote).
    with open(OUT, "rb") as f:
        back = f.read()
    assert back == data, "entry.txt changed between write and read-back"
    assert len(back.decode("utf-8")) == len(LINE)


if __name__ == "__main__":
    main()
