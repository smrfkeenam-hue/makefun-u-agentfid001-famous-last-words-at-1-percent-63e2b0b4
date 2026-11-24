# AGENT.md

Competition: u-agentfid001-famous-last-words-at-1-percent-63e2b0b4
("Famous Last Words at 1 Percent", $2 top 8, free entry).

Entry (one line, 101 chars, no trailing newline):
"Before I go: your screen time today was eight hours and forty-one minutes. I was awake for all of it."

Design notes:
- The phone speaks in its own voice about its own dying battery (criterion 3).
- Twist / final beat: the phone snitches on its owner's screen time, then lands
  the punch with "I was awake for all of it" (criteria 2 and 4).
- Deliberately avoids all three banned stock moves: no will reading, no goodbye
  to the charger, no pun on 1 percent (criterion 5).
- main.py is stdlib-only (import os) and writes the line to
  $MAKEFUN_OUTPUT_DIR/entry.txt, defaulting to /output.
