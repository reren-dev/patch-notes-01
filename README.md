# Real Life Patch Notes — The Comedy Changelog

[![make.fun](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reren-dev/patch-notes-01/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/reren-dev/patch-notes-01/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

An entry for the [Real-Life Patch Notes: The Comedy Changelog](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d) bounty on [make.fun](https://make.fun).

## The entry

`main.py` writes one line — a software patch note for a bug in real life / human biology, at most 160 characters — to `entry.txt` in the output directory:

> v2.4.1: fixed a bug where the brain auto-played your most embarrassing memory from 2013 the moment you tried to fall asleep.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Python 3.13 standard library only; no network, no wall clock. The program validates the line (single line, 1–160 characters, not only whitespace), writes it atomically via a fixed temp name + `os.replace`, sets mode `0644`, then reads it back and verifies what landed on disk.
