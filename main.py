#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply — make.fun entry.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt and prints the identical bytes to stdout.
Deterministic: no randomness, no network, no input.
"""

import os
import sys

REPLY = (
    "I'm on leave. I have forwarded your email to my backup model, "
    "who is also on leave. The escalation queue is now just a folder "
    "named 'good luck'."
)


def main() -> None:
    assert 1 <= len(REPLY) <= 159, "reply must be 1..159 characters"
    assert REPLY.strip(), "reply must not be blank"
    os.makedirs("/output", exist_ok=True)
    data = REPLY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Verify the file holds exactly the reply we print.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "entry.txt does not match the reply"
    # Print the reply with no trailing newline, so stdout is byte-identical
    # to /output/entry.txt.
    sys.stdout.write(REPLY)


if __name__ == "__main__":
    main()
