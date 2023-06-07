from Operations import G, T, N, TF_OERATIONS
from collections import deque


class Node:
    def __init__(self, type, ID):
        self._type = type
        self._ID = ID
    
    @property
    def type(self):
        return self._type
    
    @property
    def ID(self):
        return self._ID

    def extension_append(self,new_node):
        if self.type == "UserInput":
            pass
        elif self.type == "Operation":
            pass

    def back_type(self):
        if self._type == "Operation":
            pass
        elif self._type == "User_input":
            return T

def tracking_by_pos(Node_ID):
    """Find the tracks that generate current Node. Until Ends in Head. Used 
    on leaves"""
    res = deque()
    tmp = Node_ID
    while tmp != 0:
        res.appendleft(tmp)
        tmp = (tmp - 1) // 5
    res.appendleft(0)
    return list(res)


class Operation_Node(Node):
    def __init__(self, ID, Operation_ID, depth):
        super().__init__("Operation", ID)
        self._ext_seed = 1
        self.opertaion = TF_OERATIONS[Operation_ID]
        self.max_node = len(self.opertaion.relation_list) # tf.add = 2
        self.children = [None] * self.max_node
        self.depth = depth
        self.full = False

    def find_pos(self, pos):
        """
        Given a global pos.
        Used on head. Pos should include an operation.
        Often used for a pos of a parent head, when origin pos is a leaf.
        Return its reference.
        """
        assert self.check_exist(pos)
        if pos == 0:
            return self
        tracks = tracking_by_pos(pos)
        parent = self
        for id in tracks[1:]:
            parent = parent.children[(id-1)%5]
        return parent

    def check_exist(self, pos):
        """Check if the position of a Node exists or not.
        If there is an operation there, return True
        Else. return False
        Used on head"""
        if pos == 0:
            return True
        tracks = tracking_by_pos(pos)
        parent = self
        for id in tracks[1:]:
            if (id - 1) % 5 + 1  > parent.max_node:
                return False
            else:
                parent = parent.children[(id-1)%5]
            if parent == None:
                return False
        return True
        

    # def extension_Head(self, Node_ID, pos, new_OP_ID):
    #     """Append new operation to current HEAD, check if extendable.
    #     Use on the Head Node of a tree"""
    #     if Node_ID == 0:
    #         self.extension(pos, new_OP_ID)
    #         return
    #     tracks = self.tracking(Node_ID)
    #     parent = self
    #     for id in tracks[1:]:
    #         parent = parent.children[id%5-1]
    #         assert parent != None
    #     parent.extension(pos, new_OP_ID)

    def extension(self, local_pos, new_OP_ID):
        """Append new operation to current node, check if extendable.
        Use on the direct parent Node of a Leaf"""
        assert local_pos < self.max_node
        if not self.full:
            self.children[local_pos] = Operation_Node(5*self.ID+local_pos+1, new_OP_ID, self.depth+1)
        self._ext_seed += 1
        if self._ext_seed > self.max_node:
            self.full = True
    
    def renew_weight(self):
        """Assign new value according to User requirement and current structure."""
        pass

    def tracking(self):
        """Find the tracks that generate current Node. 
        Until Ends in Head.Used on leaves"""
        res = deque()
        tmp = self.ID
        while tmp != 0:
            res.appendleft(tmp)
            tmp = (tmp - 1) // 5
        res.appendleft(0)
        return list(res)

    def __repr__(self) -> str:
        """Representation of the Node
        REturn its ID and operation"""
        return "ID: " + str(self.ID) + ",Operation:" + self.opertaion.name + ",Children:" + str(self._ext_seed-1) + "\n"

    def re_express(self):
        """
        Return the expression starting from current Node,
        the unassgned Node is represented as with sub-operation relations. 
        Used on Head"""
        res = self.opertaion.name + "("
        for child in range(self.max_node):
            if self.children[child] == None:
                res += str(5*self.ID+child+1) + ", "
            else:
                res += self.children[child].re_express()
                res += ", "
        res = res[:-2]
        res += ")"
        return res
    
    def find_leaves(self):
        """Return a dict with key being the leaves's pos_ID, value being  
        the compressed sub-operation.
        Used on Head
        Example: {1:T, 2:T}
        Also, assign this to the self. Update the extension function
        """
        res = {}
        for child in range(self.max_node):
            if self.children[child] == None:
                res[5*self.ID+child+1] = self.opertaion.relation_list[child]
            else:
                res.update(self.children[child].find_leaves())
        return res
    
    def compressing_leaves(self):
        pass

    def compressing(ls: list) -> int:
        if N in ls:
            return N
        elif T in ls:
            return T
        else:
            return G




class UserInput_node(Node):
    def __init__(self, ID, Input_ID):
        super().__init__("UserInput", ID)