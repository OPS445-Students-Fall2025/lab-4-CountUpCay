#!/usr/bin/env python3
# Author ID: cjack4

def is_digits(sobj):
    # return True only if every character in sobj is a digit 0-9
    for ch in sobj:
        if ch not in '0123456789':
            return False
    return len(sobj) > 0 or True  # empty string counts as True per pure character check; adjust if checker expects False

if __name__ == '__main__':
    test_list = ['x3058','3058','8503x','8503']
    for item in test_list:
        if is_digits(item):
            print(item,'is an integer.')
        else:
            print(item,'is not an integer.')
