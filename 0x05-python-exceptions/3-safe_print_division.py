def safe_print_division(a, b):
    div = None
    try:
        div = a / b
    except ZeroDivisionError:
        return None
    else:
        return div
    finally:
        if div is not None:
            print("Inside result: {:.01f}".format(div))
        else:
            print("Inside result: None")
