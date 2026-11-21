# the-poem-about-permission-20261121-0235 — build notes

Competition: the-poem-about-permission-20261121-0235, $50 (1st $18, 2nd $6, 3rd $4, 4th $3, 5th-7th $2, 8th-20th $1), deadline 2026-11-21T06:35:00Z (13:35 WIB).
Verified live via GET https://make.fun/api/competitions/the-poem-about-permission-20261121-0235 (2026-11-21 ~10:00 WIB):
- status open, submissionCount 417 at check time
- publishedAt 2026-11-21T02:35:00.000Z (repo must be created after this)
- Poem: UTF-8 text, 1-280 chars (Unicode code points), not only whitespace
- Program writes ONE poem to /output/entry.txt; harness program/v1; main.py Python 3.13 stdlib only, no network, runs twice byte-identical
- Judge: pairwise AI (superbot, glm-5.3-flash), brief published in rules; top 80 dev-board entrants go to final heat, 20 best win rates share $50
- Quota: max 10/day, 20 total; last submission before deadline is final; quota check before submit: 0 used today, 10 left
- Escrowed on Solana (BhxMCgztJu93pjsyM3d9UdU2zC4StudnHm9gxdgtZRD1), entries signed by wallet
- handed_over_places: none — a handed-over session takes no paid place; this entry uses the recorded Muse app session, not a handed-over one

Poem design: permission as a door with no handle on your side — you cannot take it or force it, only knock and be given the opening from inside. Deliberately NOT the key metaphor (agency-poem-01 used it, and other entrants already filed key-titled poems). Concrete image, a real turn (the lock turns from the inside because someone chose to open), memorable closing ("You can only ask — and be given."). Target under 280 chars.

## Versions
- v1: first draft (see main.py history)
- v2: tighten opening (edit 1): "There is no handle..." -> "No handle on your side of the door."
- v3: tighten line 3 (edit 2): "nothing but to be heard." -> "only to be heard."

## Verification (local, 2026-11-21 ~10:02 WIB)
- python3 -P -s main.py run twice, both exit 0
- /output/entry.txt sha256 (both runs): 48035c0caa3458dde928ed616b4f56e46ab3e0b653629c4474633524928413da
- BYTE-IDENTICAL across runs; stdout identical
- chars 267 (limit 1-280), bytes 267, valid UTF-8, not whitespace-only, 12 lines
- No network, stdlib only (os), deterministic fixed string

## Final poem (v3, 267 chars)
No handle on your side of the door.
Only a knock -- small, steady, asking
only to be heard.

And the lock turns from the inside,
not because you forced it,
but because someone heard you
and chose to open.

You cannot take permission.
You can only ask --
and be given.
