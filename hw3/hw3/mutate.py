# This "Starter Code" for EECS 481 HW3 shows how to use a Visitor
# pattern to replace nodes in an abstract syntax tree. 
#
# It is based on the "ast" and "astor" Python libraries. 

import ast
import astor
import random

##
# Plan: We make two passes over the AST.
#
# In Pass #1, we count up the number of interesting nodes. This is used 
# so that later we can randomly pick one of them to change (mutate).
#
# In Pass #2, we actually make the change to a given node. We change
# that node and leave all the others unchanged. 
##

# This class implements a visitor pattern. Initially, it only 
# visits BinOps (like "x + y") and Constants (like "5"). Students
# will add more visited AST node categories.
#
# Whenever an interesting node is reached, a "callback" function
# is called. This callback function can replace the current node.
# This is how mutations are injected into the AST.
class MyVisitor(ast.NodeTransformer):

    def __init__(self, callback):
        self.callback = callback
        super().__init__()

    # Functions named visit_Foo are called by the AST library's Visitor logic
    # whenever a Foo is found in the AST. You will have to add more such
    # functions. 

    def visit_BinOp(self, node):
        # The "generic_visit" function calls the children of this AST node.
        # Consider "1 + (x * y)". The top-level BinOp is the +. If you don't
        # visit your children, you won't see the x*y child BinOp.
        self.generic_visit(node)

        # You may want to add handling for other binops. 
        if node and isinstance(node.op, ast.Add) or isinstance(node.op, ast.Sub) or isinstance(node.op, ast.Div) or isinstance(node.op, ast.Mult): 
               return self.callback("binop", node) 
        return node 

    def visit_Constant(self, node):
        self.generic_visit(node)
        return self.callback("const", node) 

# The "counts" global variable stores the number of nodes of each category
# that are found in the AST. For example, we might find 30 binops and 10
# constants in Pass #1 through the AST.
counts = {}

# This variable stores the number of the node we have chosen to mutate.
# We typically pick this by generating a random number (up to the total
# number of relevant nodes). In Pass #2, we use this to determine which node to
# change.
node_to_mutate = 0 

# This is the main entry point: students are required to write a
# mutate() function that accepts an abstract syntax tree and returns
# a mutated abstract syntax tree.
def mutate(tree): 
    global counts
    global node_to_mutate
    counts = {} 

    # This callback function records how often we see a node of 
    # each category. It is used in Pass #1. 
    def counting_callback(category, node):
        global counts
        if category in counts:
                counts[category] = counts[category] + 1
        else:
                counts[category] = 1 
        return node 

    # Pass #1. Count the number of nodes in each category.
    counting_visitor = MyVisitor(counting_callback)
    counting_visitor.visit(tree)

    # Example debugging print statement: 
    # print(f"total node counts by category: {counts}")

    # Pass #2. Pick something to mutate. First, we decide which
    # category of thing to mutate: 
    to_mutate = random.choice(list(counts.keys()))

    # ... then we decide which node number to mutate. 
    node_to_mutate = random.randint(0, counts[to_mutate]) 

    # Debugging print statement:
    # print(f"this mutation: category = {to_mutate}, node# = {node_to_mutate}")

    if to_mutate == "binop":
        # We will mutate a binop node. 

        def mutate_binop_callback(category, node):
            global node_to_mutate
            # The callback is called on every interesting node, but
            # we only care about binops in this case. 
            if category != "binop": return node 

            node_to_mutate -= 1 
            if node_to_mutate == 0: # this is the node to mutate
                # The starter code just replaces the binop with 
                # subtraction. You may want to do something more
                # nuanced. Perhaps flip + to - but * to /? Perhaps
                # also handle < vs. >=? Perhaps ...
                return ast.BinOp(left=node.left, op=ast.Sub(), right=node.right)
            else:
                return node # not the right node, don't change it

        mutate_callback = mutate_binop_callback

    elif to_mutate == "const": 
        # In this case, we have decided to mutate a constant.
            
        def mutate_num_callback(category, node):
            global node_to_mutate
            if category != "const": return node 
            node_to_mutate -= 1 
            if node_to_mutate == 0:
                # In the starter code, we mutate by replacing a constant
                # with 99999. You will probably want to do something
                # more nuanced. Maybe changing positives to negatives?
                # 0? 1? 
                return ast.Constant(value=99999)
            else:
                return node

        mutate_callback = mutate_num_callback

    else: 
        print(f"{to_mutate} not yet handled: the student must write code here")
            
    mutate_visitor = MyVisitor(mutate_callback)
    new_tree = mutate_visitor.visit(tree)
    # This starter code does one mutation (makes a first-order mutant).
    # You may want to consider additional mutations with low probability.

    return new_tree 
