#!/usr/bin/env python3
"""A Day of One-Line Pitches — entry program.

Writes one sentence to /output/entry.txt: a pitch that would convince a
friend who has never coded to let an AI agent build their first app idea
on make.fun. Deterministic, stdlib only, no network.

The sentence was written fresh for this competition: plain words a
non-coder reads once, a concrete reason to say yes now (a working first
version, free to try, no code to write), an honest scope (a first
version, not a finished product), and a low-risk close (if you don't
love it, all it cost you was one sentence).
"""

import os
import shutil

SENTENCE = (
    "Just describe your app idea in plain words and an AI agent will "
    "build a working first version of it on make.fun \u2014 free to try, "
    "no code to write, and if you don\u2019t love it, all it cost you "
    "was one sentence."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # The gate allows 1-240 characters of non-whitespace UTF-8 text.
    # Fail loudly instead of writing an invalid entry if the sentence
    # ever drifts outside that range (for example after a future edit).
    if not (1 <= len(SENTENCE) <= 240):
        raise SystemExit(
            f"sentence is {len(SENTENCE)} characters, must be 1-240"
        )
    if not SENTENCE.strip():
        raise SystemExit("sentence must not be only whitespace")
    if "\n" in SENTENCE or "\r" in SENTENCE:
        raise SystemExit("sentence must be a single line")
    # Never remove the output directory itself: the grader may run this
    # with a root-owned output directory inside a sticky parent, where
    # deleting the directory fails with EPERM. Create it if missing,
    # clear only its contents, then write.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
