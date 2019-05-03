#!/usr/bin/python3
if __name__ == "__main__":
    operators = ["+", "-", "*", "/"]
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    op = sys.argv[2]
    if op in operators:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if operators.index(op) == 0:
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
        if operators.index(op) == 1:
            print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
        if operators.index(op) == 2:
            print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
        if operators.index(op) == 3:
            print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
