#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short family scene (1-2 lines, 1-280 UTF-8 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only. No network, no input files.
"""
import os
import sys
from pathlib import Path

ENTRY = (
    "When the power went out, we ate dinner by candlelight and my six-year-old "
    "whispered, \"It's like a restaurant, but the waiter is Dad and he's "
    "terrible.\" Dad bowed. We tipped him in hugs."
)


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("refusing to write: entry is blank", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"refusing to write: entry is {len(text)} characters", file=sys.stderr)
        return 1
    if text.count("\n") + 1 > 2:
        print("refusing to write: entry is more than 2 lines", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
