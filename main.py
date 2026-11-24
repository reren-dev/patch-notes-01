"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch note -- a funny changelog entry for a bug in real
life / human biology -- to entry.txt in the output directory.

Usage (as graded by make.fun program/v1):
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
"""

import os

# The entry: one line, at most 160 characters, in the terse register of a
# real release note. A specific, recognisable bug of the body: the brain
# auto-playing an old embarrassment the moment you try to sleep.
LINE = (
    "v2.4.1: fixed a bug where the brain auto-played your most embarrassing "
    "memory from 2013 the moment you tried to fall asleep."
)

MAX_CHARS = 160


def main() -> None:
    line = LINE

    # Validate: exactly one line, 1..160 characters, not only whitespace,
    # no control characters other than the line break we add on write.
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("entry must not contain control characters")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not out_dir:
        raise RuntimeError("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")

    # Write via a fixed temp name, then atomically replace, so the output
    # directory never holds anything but entry.txt (no random temp files).
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)

    # Read it back and verify what landed on disk.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise RuntimeError("entry.txt on disk does not match the entry")
    if len(written.rstrip("\n")) > MAX_CHARS:
        raise RuntimeError("entry.txt exceeds the character limit")

    print("wrote entry.txt (%d chars)" % len(line))


if __name__ == "__main__":
    main()
