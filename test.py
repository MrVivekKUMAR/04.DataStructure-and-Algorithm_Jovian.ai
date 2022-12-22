def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))