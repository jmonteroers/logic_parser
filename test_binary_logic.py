from binary_logic import parse_expression_with_parentheses

def test_parse_expression_with_parentheses_empty():
    expression = "hey you OR"
    assert parse_expression_with_parentheses(expression) == (
        [], "OR"
    )

def test_parse_expression_with_parentheses_simple():
    expression = "(hey you OR) (hey there AND) AND"
    assert parse_expression_with_parentheses(expression) == (
        ["hey you OR", "hey there AND"], "AND"
    )


def test_parse_expression_with_parentheses_complex_deep():
    expression = "(hey you (dear myself OR) AND) (there (here NOT) AND) OR"
    assert parse_expression_with_parentheses(expression) == (
        ["hey you (dear myself OR) AND", "there (here NOT) AND"], "OR"
    )

def test_parse_expression_with_parentheses_complex_deep_multiple():
    expression = "(hey you (dear myself OR) AND) (there (here NOT) AND) ((why not) (here NOT) AND) (huawei NOT) OR"
    assert parse_expression_with_parentheses(expression) == (
        ["hey you (dear myself OR) AND", "there (here NOT) AND",
         "(why not) (here NOT) AND", "huawei NOT"], "OR"
    )