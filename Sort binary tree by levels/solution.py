def tree_by_levels(node):
    if node is None:
        return []
    queue = [node]
    res = []
    while queue:
        if queue[0]:
            queue.append(queue[0].left)
            queue.append(queue[0].right)
            res.append(queue[0].value)
        queue.pop(0)
    return res
