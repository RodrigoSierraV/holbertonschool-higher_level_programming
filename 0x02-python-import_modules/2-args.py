#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    b = len(sys.argv) - 1
    if b == 0:
        print("0 arguments.")
    else:
        print("{:d} {}".format(b, "argument:" if b == 1 else "arguments:"))
    for i in range(1, b + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
