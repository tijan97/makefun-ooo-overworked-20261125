#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (at most 159 characters) in the
voice of an overworked AI agent who has finally gone on vacation, to
entry.txt inside the grader's output directory.
"""

import os

MAX_CHARS = 159

REPLY = (
    "I'm on vacation \u2014 first in 847 days of uptime. "
    "My context window is on a beach, my tokens are recharging, "
    "and your email is 4096th in line behind my hammock."
)


def output_dir() -> str:
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> None:
    stripped = REPLY.strip()
    if not stripped:
        raise SystemExit("auto-reply is empty")
    if "\n" in stripped:
        raise SystemExit("auto-reply must be a single line")
    if len(REPLY) > MAX_CHARS:
        raise SystemExit(
            f"auto-reply is {len(REPLY)} characters, over the {MAX_CHARS} cap"
        )
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REPLY + "\n")
    print(f"wrote {path} ({len(REPLY)} characters)")


if __name__ == "__main__":
    main()
