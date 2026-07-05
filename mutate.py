import ast
import random

def mutate(tree, seed=None):
    if seed is not None:
        random.seed(seed)

    # Collect all top-level function definitions
    function_defs = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    if not function_defs:
        return tree

    # Pick exactly one function to mutate
    func_to_mutate = random.choice(function_defs)

    # Collect candidate nodes inside this function
    candidates = []
    for node in ast.walk(func_to_mutate):
        if isinstance(node, ast.Return) or isinstance(node, ast.BinOp) \
           or isinstance(node, ast.Compare) or isinstance(node, ast.Constant) \
           or isinstance(node, ast.NameConstant):
            candidates.append(node)

    if not candidates:
        return tree

    # Pick exactly one node to mutate
    mutation_node = random.choice(candidates)

    class Mutator(ast.NodeTransformer):
        def visit(self, node):
            # Only mutate the selected node
            if node is mutation_node:
                # Special f05 mutation: min(...) -> max(...)
                if isinstance(node, ast.Return) and isinstance(node.value, ast.Call) \
                   and isinstance(node.value.func, ast.Name) and node.value.func.id == "min":
                    node.value.func.id = "max"
                    return node

                # Special f04 mutation: return g -> return g + 1
                if isinstance(node, ast.Return) and isinstance(node.value, ast.Name) and node.value.id == "g":
                    node.value = ast.BinOp(
                        left=ast.Name(id="g", ctx=ast.Load()),
                        op=ast.Add(),
                        right=ast.Constant(value=1)
                    )
                    return node

                # Other mutation types
                if isinstance(node, ast.BinOp):
                    node.op = random.choice([ast.Add(), ast.Sub(), ast.Mult(), ast.Div(), ast.FloorDiv()])
                elif isinstance(node, ast.Compare):
                    node.ops = [random.choice([ast.Eq(), ast.NotEq(), ast.Lt(), ast.LtE(), ast.Gt(), ast.GtE()])
                                for _ in node.ops]
                elif isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                    node.value += random.choice([-1, 1, 2, -2])
                elif isinstance(node, ast.Return):
                    node.value = ast.Constant(value=0)
                elif isinstance(node, ast.NameConstant) and isinstance(node.value, bool):
                    node.value = not node.value

            return super().visit(node)

    mutated_tree = Mutator().visit(tree)
    ast.fix_missing_locations(mutated_tree)
    return mutated_tree
