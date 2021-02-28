# logic_parser
Python package to save complex logic as text (notice, work in progress!)

All the functions work with a list of values, and an expression. The simplest expression is a string, where parentheses and logical words ("OR", "AND", "NOT") are reserved words.
To evaluate the boolean value of a string, it is simply checked whether the string belongs to the list of values provided.

For example,
```
values = ["hey", "Jude"]
binary_logic.rpn_logic("hey") == True 
binary_logic.rpn_logic("why") == False 
```

To move from simple expressions to more complex, you can use logical operators "OR", "AND", "NOT" at the end of an expression ("AND" assumed by default if no logical expression 
is provided). Notice that you can use as many simple expressions
as you want, separated by spaces. For example,
```
binary_logic.rpn_logic("hey you too OR") == True
binary_logic.rpn_logic("Jude you too AND") == False
binary_logic.rpn_logic("Jude you too") == False  # use AND by default
```

But this is not everything. You can make arbitrarily complex logical statements by using parentheses and the function `binary_logic.complex_rpn_logic`. For example
```
binary_logic.complex_rpn_logic("(hey you too OR) (Jude you too OR) AND") == True
```

Note that in complex logical operators, you must always specify a logical operator at the end of the expression. Otherwise, you'll get errors.


## To-do
- Create test suite for the logic
  - Rearrange tests in test_binary_logic
- Add test chapter to README
- Allow arbitrary use of newlines to write formulas
- Create Expression class?
- use tree structure to parse and then evaluate?
