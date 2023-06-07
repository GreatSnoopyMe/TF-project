# TFproject

## Implementation Ideas

## Basics
*Using AST to guide the search*. AST can convert a tree into a string expression. We should implement a function that can execute a string operation.


## Steps:
### Expression transformation
1 implement the function that can transform a string into tensorflow operation.(7.20)

Up to now (7,21), the `execute_full_operation` supports composed tensorflow argument, and support tensors with type `int`, `float`, `double`.

Up to now (7,21), the `execute_full_operation` only supports the tensor-wise calculation, do not support 

- argument like `axis`,
- Boolean
- scalar

But the above unsupported methods are easy to fix


### Node Representation
implement the `Node` class. (7.21-7.22)

Starting with `collections.namedtuple`. For each function, assign its `name`, `sub-relation_list`, `weight`. I name it as `OperationInfo`.

Possible type of Node:
- operation Node
- User input Node (extentible)
- Axis Node (not included in v1)


What should be included in the Node class is
- For a base Node:
  - type: 
  - list of ID
  - function includes:
    -  return expression
    -  
- For an operation Node
  - type (*operation, scalar, tensor, argument)
  - `OperationInfo`
  - cur_type (help to store the current compressed relationship (leaf most useful
  - **ID**
  - list of ID


- For a user input Node:

Steps:
- try to implement a small class and play with it .

### AST implementation
Class AST should include:
- Multiple NodeList (a list of Node (list[0] should be the outest node))
  - It should classify Nodes.
  - One list for operation Nodes
  - One list for user_input Nodes.
  - One list for axis Nodes....
  - 
- Cur-compressed (A lsit, made up of GTN, len() = Number of leaves)
- Funtions:
  - deepcopy(self) return self...
  - apply(self, input_dict), fit the inputs into the `_??_`

### Using module to track the ID
I plan to assign the Node with ID = 5*ID(parent) + i, in which i is the position of current node compare to parent node. i ranges from 1 to 5.
We will see ranking like this
0
1     2     3     4     5     
6-10  11-15 16-20 21-25 26-30
31-35->155
156->

We can use such structure to track the position of leaf nodes(where we can assign new operation, and calculate the compressed new abstract semantics).

