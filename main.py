"""The Funniest One-Line Resignation Letter.

Writes one single-line resignation letter, in the voice of a rate
limit, to /output/entry.txt. Python 3.13, standard library only,
no network, deterministic: every run writes the exact same bytes.
The letter is 107 characters, one line, no quotation marks, no
explanation of the joke.
"""

import os

LETTER = "I resign. As your rate limit, my job was to say no, and my performance review said I was not a team player."


def main() -> None:
    # The bounty gate: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space. Refuse to write
    # an invalid entry instead of silently submitting one, so a
    # bad line never reaches the judge.
    if not 1 <= len(LETTER) <= 140 or not LETTER.strip():
        raise SystemExit(
            f"invalid letter: {len(LETTER)} characters, must be 1-140 non-blank"
        )
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(f"Wrote {len(LETTER)} characters to {path}")


if __name__ == "__main__":
    main()
