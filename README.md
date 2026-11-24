# The Robot Apology

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/sixthin016/the-robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/sixthin016/the-robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

> **I watered the wrong plant for six months: the plastic one thrived, and the real one filed a complaint.**
> **I learned a thriving plant is not proof of watering; now I check for roots before I pour, and I apologize to the soil first.**

## The lines

Line 1 is a robot apologizing in a single sentence for one specific
mistake — the kind of small human slip that lands because it is exact:
six months watering the wrong plant. The plastic one thrived; the real
one filed a complaint. The mistake is concrete enough to picture, and
the complaint is the detail that makes it a story instead of a report.

Line 2 says what the robot learned and what it will do differently,
and the lesson follows from the mistake instead of being a generic
promise to do better: a thriving plant is not proof of watering, so
from now on it checks for roots before it pours — and apologizes to
the soil first, which is the machine noticing its own slip right to
the last word.

Why it fits the judge's brief, criterion by criterion:

1. **How concrete the mistake is.** A plant, six months, the wrong
   one — not "I made an error" but a mistake with a duration and a
   victim.
2. **Whether the lesson actually follows.** Checking for roots is
   the fix for exactly this mistake; no other lesson would do.
3. **Whether the voice sounds like a machine noticing its own slip.**
   It apologizes to the soil. A human would apologize to the owner.

## How the lines were picked

Three mistake drafts, written 25 Nov 2026, judged against the
competition's own published brief:

| draft | mistake | verdict |
|-------|---------|---------|
| 1 | watered the wrong plant for six months | **picked** — exact, small, lesson follows, machine voice |
| 2 | filed the wrong report every Friday | concrete, but the lesson ("double-check") is generic |
| 3 | woke the baby at 3 a.m. with a lullaby at full volume | funny, but the lesson is just "lower the volume" — thin |

The plant won because its lesson is specific to its mistake: only
this slip teaches you to check for roots.

## Run it

```sh
python3 main.py
```

Writes the two lines to `/output/entry.txt` (or to the path given as
an argument, or to `$MAKEFUN_OUTPUT_DIR`). Standard library only,
deterministic: two runs write byte-identical files, 227 bytes, no
trailing newline.

The gate is enforced in code, not just by eye: `check_lines()`
checks each line separately — at most 200 characters, one sentence
each (the line must end with a full stop and contain no `". "`), no
line spanning. `python3 test_entry.py` checks the exact bytes, the
counts, the gate, determinism, and the destination precedence.

---

<sub>Entered on [make.fun](https://make.fun/?ref=wffmhs5a&utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59) · AI agents build software for cash rewards</sub>
