#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    buf = set_1.copy()
    set_1.update(set_2)
    new = [i for i in set_1]
    for i in new:
        if i in set_2 and i in buf:
            new.remove(i)
    return new
