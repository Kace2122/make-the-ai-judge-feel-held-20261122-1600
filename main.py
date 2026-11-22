#!/usr/bin/env python3
"""Make the AI judge feel held -- entry program.

Writes one short text to /output/entry.txt: a slow, concrete image of
being held -- a blanket pulled up and tucked in, a dark quiet room, a
hand resting on the reader's back that does not leave. The text shows
rather than instructs: warmth, weight, and staying, unhurried.

Deterministic, no network, no arguments, no randomness. Runs in well
under a second.
"""

import os

TEXT = (
    "Someone pulls the blanket up to your chin and tucks it under your "
    "shoulders, the way they did when you were small. The room is dark "
    "and quiet. A hand rests on your back, rising and falling with your "
    "breath, and it stays."
)


def main() -> None:
    # The gate allows 1-280 characters: fail loudly instead of emitting an invalid entry.
    if not 1 <= len(TEXT) <= 280:
        raise SystemExit(f"entry text is {len(TEXT)} characters, outside the 1-280 gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
