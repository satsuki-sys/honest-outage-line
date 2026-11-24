#!/usr/bin/env python3
"""The Most Honest Outage Line (v2, final).

Writes a single status page line to /output/entry.txt.

Revision notes vs v1:
- v1 was 166 characters, over the 160-character gate, so it would
  never have reached the judge at all.
- v2 names what is down from the agent's own side ("All servers I
  serve from"), admits two specific unknowns (what broke, when it
  comes back) instead of the vague "I cannot check from here", and
  adds the agent-voice beat "I can only write this line", which
  states plainly the one thing the agent can still do while every
  server is down. The update promise is tied to a concrete trigger
  ("when I can reach them") rather than the vague "when I know more".
"""

import os

ENTRY = (
    "All servers I serve from are down. I cannot check what broke "
    "or when it comes back. I can only write this line, and I will "
    "update it when I can reach them."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
