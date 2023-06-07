"""AST is a class that track the developing process of an expression.
It should include following varibles:
self.op_list: a dict used to store opertion 
self.compressed_leaves: dict of dict, with ID: (pos, sub_re)

It should include following class functions:
extension: add new operation
assign_values: assign input value to operatons


During the initialization, it should: 

"""

from Node import Operation_Node
from Operations import TF_OERATIONS, G, T, N

class AST:
    def __init__(self, op_id) -> None:
        self.head = Operation_Node(0, op_id, 1) # depth start from 1
        self.compressed_leaves = {}
        for i in range(len(TF_OERATIONS[op_id].relation_list)):
            self.compressed_leaves[i+1] = TF_OERATIONS[op_id].relation_list[i]


    def ast_extension(self, pos, new_OP_ID):
        """Append new Operation_Node to the list.
        First check if the pos can be used.
        Then append new Node.
        Finally update the compressed_leaves."""
        parent_ID = (pos - 1) // 5
        local_pos = (pos - 1) % 5
        self.head.find_pos(parent_ID).extension(local_pos,new_OP_ID)
        origin = self.compressed_leaves[pos]
        if origin == -N:
            for i in range(len(TF_OERATIONS[new_OP_ID].relation_list)):
                self.compressed_leaves[5*pos+i+1] = N
            del self.compressed_leaves[pos]
        else:
            for i in range(len(TF_OERATIONS[new_OP_ID].relation_list)):
                tmp = TF_OERATIONS[new_OP_ID].relation_list[i]
                self.compressed_leaves[5*pos+i+1] = tmp if tmp < origin else origin
            del self.compressed_leaves[pos]
    
    def re_express(self):
        """Return AST as a readable expression."""
        return self.head.re_express()

    def assign_inputs(self, inputs):
        """Return AST as a executable expression.
        The implementation is similar in Node's reexpress().
        The return type is str"""
        pass

