#!/usr/bin/env python3
"""The Robot Apology.

Writes two lines to ``entry.txt``: a robot confessing one specific
mistake, then the lesson it learned and what it will do differently.

The mistake is exact and small: the robot watered the wrong plant for
six months -- the plastic one thrived, the real one filed a complaint.
The lesson follows from the mistake instead of being a generic promise
to do better: a thriving plant is not proof of watering, so from now
on the robot checks for roots before it pours, and apologizes to the
soil first. The voice is a machine noticing its own slip, in two
sentences, with no setup outside them.

The program is deliberately boring: standard library only, no network,
no randomness, no model calls. It checks both lines against the
competition gate (UTF-8, one sentence each, at most 200 characters
per line) and writes exactly those bytes, joined by a single newline
and with no trailing newline, so the byte count the judge's tie-break
reads is the two lines themselves.

Output destination, in order:
  1. the first command-line argument, when given;
  2. ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the variable is set;
  3. ``/output/entry.txt``.
"""

import os
import sys

# Line 1: one specific mistake -- six months watering the wrong plant.
# Line 2: the lesson, which follows from that mistake -- check for
# roots before pouring.
LINES = (
    "I watered the wrong plant for six months: the plastic one thrived, and the real one filed a complaint.",
    "I learned a thriving plant is not proof of watering; now I check for roots before I pour, and I apologize to the soil first.",
)

MAX_CHARS = 200
MIN_CHARS = 1
DEFAULT_PATH = "/output/entry.txt"
FILE_NAME = "entry.txt"


def check_lines(lines):
    """Return gate problems for *lines* (empty list means they pass)."""
    problems = []
    if len(lines) != 2:
        problems.append(
            "entry must have exactly two lines, got %d" % len(lines)
        )
    for index, line in enumerate(lines, start=1):
        if not isinstance(line, str):
            problems.append("line %d is not text" % index)
            continue
        if len(line) < MIN_CHARS:
            problems.append("line %d is empty" % index)
        if len(line) > MAX_CHARS:
            problems.append(
                "line %d is %d characters, over the %d-character limit"
                % (index, len(line), MAX_CHARS)
            )
        if line.strip() == "":
            problems.append("line %d is only whitespace" % index)
        if "\n" in line or "\r" in line:
            problems.append("line %d spans more than one line" % index)
        # The brief wants one sentence per line, so enforce it: a line
        # must end with a full stop and hold no ". " inside it.
        if not line.endswith("."):
            problems.append("line %d does not end with a full stop" % index)
        if ". " in line:
            problems.append("line %d contains more than one sentence" % index)
        try:
            line.encode("utf-8")
        except UnicodeEncodeError:
            problems.append("line %d is not valid UTF-8" % index)
    return problems


def pick_path(argv):
    """Choose where entry.txt goes: argv, env var, then the default."""
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return os.path.join(env_dir, FILE_NAME)
    return DEFAULT_PATH


def save(path, lines):
    """Validate *lines* and write them as exact UTF-8 bytes."""
    problems = check_lines(lines)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    text = "\n".join(lines)
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    print(text)
    print(
        "wrote %d lines / %d bytes to %s" % (len(lines), len(data), path)
    )
    return 0


def main(argv):
    return save(pick_path(argv), LINES)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
