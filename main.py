#!/usr/bin/env python3
"""Entry for make.fun bounty u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.

Writes one roast line (<=160 chars) to /output/entry.txt.
Deterministic: no randomness, no network, no time dependence.
"""

import os

ENTRY = (
    "My smart fridge has a camera, a touchscreen, and the audacity "
    "to suggest a salad every time I reach for the cake."
)

# Gate guard: the sealed scorer requires 1-160 UTF-8 chars, one line,
# not only whitespace. Fail loudly here rather than shipping an invalid entry.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, gate is 1-160"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the text, no trailing newline, so the gate counts
    # precisely the characters of the line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
