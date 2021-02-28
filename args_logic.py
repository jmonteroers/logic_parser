from operator import __or__, __and__


def and_args(*args):
    if len(args) < 2:
        raise(ValueError("at least 2 values must be provided"))
    current_value = True
    for val in args:
        current_value = __and__(
            current_value,
            val
        )
    return current_value


def or_args(*args):
    if len(args) < 2:
        raise(ValueError("at least 2 values must be provided"))
    current_value = False
    for val in args:
        current_value = __or__(
            current_value,
            val
        )
    return current_value