#!/usr/bin/env python

import sys
import numpy as np

def main(encoded_phrase):
    def unapply_cipher(c, key):
        is_capital_letter = c.isupper()
        start_pos = 65 if is_capital_letter else 97
        return chr(start_pos + (ord(c) - start_pos + (26 - key)) % 26)

    letter_freq = []

    for c in encoded_phrase:
        if c.isalnum() and c.isupper():
            letter_freq.append(ord(c) - 65)
        if c.isalnum() and c.islower():
            letter_freq.append(ord(c) - 97)

    bincount = np.bincount(letter_freq)

    key = (bincount.argsort()[-1] - ((ord('e') - 97))) % 26

    phrase = ""
    for c in encoded_phrase:
        if c.isalnum():
            phrase = phrase + unapply_cipher(c, key)
        else:
            phrase = phrase + c

    print(phrase)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide encrypted message as a first commandline argument.')
        sys.exit(1)
    main(sys.argv[1])