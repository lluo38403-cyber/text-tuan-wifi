"""One Word for Your Wi-Fi — make.fun entry.

Writes one word to /output/entry.txt: a single word, at most 20
characters, describing my Wi-Fi. The word is both the funniest and the
truest one I can offer — fast Wi-Fi in this house is a legend everyone
has heard of and nobody has ever actually seen.
"""

import os

ENTRY = "Mythical"

MAX_CHARS = 20


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single word"
    assert " " not in text, "entry must be a single word"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
