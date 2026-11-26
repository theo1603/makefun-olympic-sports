"""Rejected Olympic Sports entry.

Writes one funny single-line sport the Olympics turned down to
/output/entry.txt. Deterministic, standard library only, no network.

Revision notes (v2): tightened the setup and added a second punch.
"stand" -> "hold" (more athletic, more formal), added the concrete
setting "at a bus stop" so the scene reads like a broadcast, "never
arrives" -> "never comes" (shorter, punchier), and a silver-medal
kicker ("tuts loudest") so the joke lands twice instead of once.
"""

import os

LINE = (
    "Synchronised Queueing: four athletes hold perfect formation at a "
    "bus stop for a bus that never comes; gold goes to whoever complains "
    "least, silver to whoever tuts loudest."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
