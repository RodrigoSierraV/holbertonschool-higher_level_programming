def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        return div
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(div))