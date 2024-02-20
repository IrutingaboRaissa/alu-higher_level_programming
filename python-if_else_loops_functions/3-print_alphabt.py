#!/usr/bin/python3
for ascii_code in range(ord('a'), ord('z')+1):
    if chr(ascii_code) not in 'qe':
        print("{}".format(chr(ascii_code)), end='')
