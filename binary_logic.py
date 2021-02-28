# adaptation for logic operators
# given a list, checks whether given characters belong to the string

from args_logic import and_args, or_args
from operator import __not__

LOGICAL_OPS = {
    "AND": and_args,
    "OR": or_args,
    "NOT": __not__
}

def rpn_logic(expression, values: list, operators=LOGICAL_OPS):
    tokens = expression.split()
    stack = []
    for token in tokens:
        if token in operators:
            return operators[token](*stack)
        else:
            stack.append(token in values)
    return operators["AND"](*stack)

def complex_rpn_logic(expression, values, operators=LOGICAL_OPS):
    """
    recursive algorithm to evaluate deeper logic
    :param expression:
    :param values:
    :param operators:
    :return:
    """
    # terminal condition
    if not "(" in expression:
        return rpn_logic(expression, values)
    simpler_expressions, operator_name = parse_expression_with_parentheses(expression)
    logical_operator = operators[operator_name]
    boolean_values = [
        complex_rpn_logic(simpler_expression,
                          values=values)
        for simpler_expression in simpler_expressions
    ]
    return logical_operator(*boolean_values)


def parse_expression_with_parentheses(expression):
    operator = expression.split()[-1]
    simpler_expressions = []
    current_expression = ""
    open_parentheses = 0
    for char in expression:
        # counting parentheses
        if char == "(":
            open_parentheses += 1
            # if beginning parentheses, continue
            if open_parentheses == 1:
                continue
        elif char == ")":
            open_parentheses -= 1
            # ending parentheses
            if open_parentheses == 0 and current_expression:
                simpler_expressions.append(current_expression)
                current_expression = ""
                continue
        # adding characters
        if open_parentheses:
            current_expression += char
    # clean original expression of all expressions within parentheses
    for simpler_expression in simpler_expressions:
        expression = expression.replace(
            simpler_expression,
            ""
        )
    expression = expression.replace(
        "(",
        ""
    ).replace(
        ")",
        ""
    )
    # add remaining simpler expressions
    simpler_expressions += expression.split()[:-1]
    return simpler_expressions, operator


if __name__ == "__main__":
    values = ["jaggerbomb", "vodka", "beer"]
    print(complex_rpn_logic("whisky NOT", values=values))
    print(complex_rpn_logic("vodka beer AND", values=values))
    print(complex_rpn_logic("vodka jagger AND", values=values))
    print(complex_rpn_logic("lemon jagger OR", values=values))
    print(complex_rpn_logic("lemon jaggerbomb OR", values=values))
    print(complex_rpn_logic("(vodka beer (dear myself OR) AND) ((jaggerbomb here Miguel AND) NOT) OR",
                            values=values))
    print(complex_rpn_logic("(jaggerbomb here Miguel OR) NOT",
                            values=values))