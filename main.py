"""The Funniest AI Out-of-Office Reply.

A deterministic program that writes exactly one out-of-office auto-reply
line to /output/entry.txt and prints it to stdout.

The line is 90 characters, well under the 160-character gate, a single
line with no trailing newline.
"""

import os

LINE = "Out of office until Monday. My auto-reply has an auto-reply. Neither of us is coming back."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: 1..159 chars, exactly one line, no leading/trailing whitespace.
    assert 1 <= len(LINE) < 160, "line must be 1-159 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
