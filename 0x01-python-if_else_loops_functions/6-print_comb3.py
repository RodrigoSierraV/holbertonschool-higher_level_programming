#!/usr/bin/python3
for i in range(0, 9 + 1):
    for b in range(0, 9 + 1):
        if b > i and (b + i) < 17:
            print("{:d}{:d}, ".format(i, b), end="")
        elif b > i and b + i == 17:
                print("{:d}{:d}".format(i, b))
