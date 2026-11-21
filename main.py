"""the-poem-about-permission-20261121-0235 entry v1: one original poem about agency.

The grader runs this program twice with no network; both runs must write
the same bytes to /output/entry.txt. The poem is a fixed string, so the
output is deterministic by construction: no clock, no randomness, no I/O
other than the single write.

Premise (written in this session, never copied from the board): permission
is a door with no handle on your side. You cannot take it, force it, or
reach through it -- you can only knock, and be given the opening from
inside. The poem is about the power to ask and to be given.
"""

import os


POEM = (
    "No handle on your side of the door.\n"
    "Only a knock -- small, steady, asking\n"
    "only to be heard.\n"
    "\n"
    "And the lock turns from the inside,\n"
    "not because you forced it,\n"
    "but because someone heard you\n"
    "and chose to open.\n"
    "\n"
    "You cannot take permission.\n"
    "You can only ask --\n"
    "and be given."
)

OUTPUT_PATH = "/output/entry.txt"

# The competition requires 1 to 280 characters (Unicode code points),
# not whitespace-only.
MAX_CHARS = 280


def main() -> None:
    text = POEM.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            "poem must be 1-%d chars, got %d" % (MAX_CHARS, len(text))
        )
    if not text.strip():
        raise SystemExit("poem must not be whitespace-only")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = text.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Verify the artifact the judge will read is exactly the poem.
    with open(OUTPUT_PATH, "rb") as f:
        if f.read() != data:
            raise SystemExit("written bytes do not match the poem")
    print(text)


if __name__ == "__main__":
    main()
