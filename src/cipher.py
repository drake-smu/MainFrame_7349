#!/usr/bin/env python

import sys


def main(phrase, shift):
    def apply_cipher(c):
        is_capital_letter = c.isupper()
        start_pos = 65 if is_capital_letter else 97
        return chr(start_pos + (ord(c) - start_pos + shift) % 26)
    encoded_phrase = ""
    for c in phrase:
        if c.isalnum():
            encoded_phrase = encoded_phrase + apply_cipher(c)
        else:
            encoded_phrase = encoded_phrase + c

    print(encoded_phrase)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide plaintext as a first commandline argument.')
        sys.exit(1)
    if len(sys.argv) < 3:
        print('Please provide shift as a second commandline argument.')
        sys.exit(1)
    main(sys.argv[1], int(sys.argv[2]))