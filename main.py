"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800,
to /output/entry.txt.

The sentence is a fixed, hand-written text: deterministic, offline, no
randomness, no network. Every run writes exactly the same bytes.
"""

import os

SENTENCE = "Picture one road joining every post office and library in the world, so a letter sent from any door can be read at any other before its ink is dry."


def main():
    # The gate accepts 1 to 200 characters of UTF-8 text, not only
    # whitespace. Fail loudly here rather than shipping a bad entry.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    assert SENTENCE.strip() == SENTENCE, "no leading/trailing whitespace"
    assert SENTENCE.count(".") == 1, "exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
