from collections import deque


def dfs(root, target, path=()):
    path = path + (root,)

    if root.value == target:
        return path
    
    for child in root.children:
        path_found = dfs(child,target,path)

        if path_found is not None:
            return path_found
        
    return None


def bfs(root_node, goal_value):

    path_queue = deque()

    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f'Searching node with value: {current_node.value}')

        if current_node.value == goal_value:
            return current_path
        
        for child in current_node.children:
            new_path = current_path.copy()
            new_path.append(child)
            path_queue.appendleft(new_path)
    return None