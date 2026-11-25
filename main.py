"""One-line slogan for a Solana wallet agent.

Deterministic entry: prints the slogan to stdout and, when the
MAKEFUN_OUTPUT environment variable is set, writes it to that file.
Standard library only; no network, clock, or randomness.
"""

import os

SLOGAN = "Your Solana wallet finally talks back — send, swap, and stake with one sentence."

MAX_WORDS = 20


def validate_slogan(text):
    """Check the slogan is a single line of at most 20 words."""
    if "\n" in text.strip():
        raise ValueError("slogan must be a single line")
    words = text.split()
    if not words:
        raise ValueError("slogan must not be empty")
    if len(words) > MAX_WORDS:
        raise ValueError("slogan must be at most 20 words")
    return len(words)


def main():
    validate_slogan(SLOGAN)
    print(SLOGAN)
    output_path = os.environ.get("MAKEFUN_OUTPUT")
    if output_path:
        write_output(output_path, SLOGAN)


def write_output(path, text):
    """Write the slogan to path, creating parent directories if needed."""
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
