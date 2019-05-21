#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    div = i = 0
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("wrong type")
        except ValueError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        finally:
            new.append(div)
        i += 1
    return new
