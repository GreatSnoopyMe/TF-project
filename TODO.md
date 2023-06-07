# Implementation Ideas

## Basics
*Using AST to guide the search*. AST can convert a tree into a string expression. We should implement a function that can execute a string operation.


## Steps:
1 implement the function that can transform a string into tensorflow operation.(7.20)

Up to now (7,21), the `execute_full_operation` supports composed tensorflow argument, and support tensors with type `int`, `float`, `double`.

Up to now (7,21), the `execute_full_operation` only supports the tensor-wise calculation, do not support 

- argument like `axis`,
- Boolean
- scalar

But the above unsupported methods are easy to fix

2 implement the `Node` class. (7.21-7.22)
