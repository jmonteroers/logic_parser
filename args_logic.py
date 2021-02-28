from operator import __or__, __and__


def and_args(*args):
    if len(args) < 1:
        raise(ValueError("at least 1 value must be provided"))
    elif len(args) < 2:
        return args[0]
    current_value = True
    for val in args:
        current_value = __and__(
            current_value,
            val
        )
    return current_value


def or_args(*args):
    if len(args) < 1:
        raise(ValueError("at least 1 value must be provided"))
    elif len(args) < 2:
        return args[0]
    current_value = False
    for val in args:
        current_value = __or__(
            current_value,
            val
        )
    return current_value


def in_args(values, *args):
    """
    apply in values to all args, connect with and
    :param args:
    :return:
    """
    return and_args(*[arg in values for arg in args])