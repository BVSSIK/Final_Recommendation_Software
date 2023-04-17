from collections import deque
from linked_list import LinkedList


def dfs(root, target, path=()):
    path = path + (root,)

    if root.value == target:
        return path

    if type(root.value) == LinkedList:
        linked_list_check = linear_search(root, path, target)
        if linked_list_check != None:
            return linked_list_check


    
    for child in root.children:
        path_found = dfs(child,target,path)

        if path_found is not None:
            return path_found
        
    return None


def bfs(root_node, goal_value):

    path_queue = deque()
    path_print = []

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
        
        if type(current_node.value) == LinkedList:
            linked_list_check = linear_search(current_node, current_path, goal_value)
            if linked_list_check != None:
                return linked_list_check

            # print(f'Entering linked list {current_node.value.get_head_node().get_value()}')
            # current_node = current_node.value.get_head_node()
            # while current_node.get_next_node():
            #     current_node = current_node.get_next_node()
            #     if current_node.name == goal_value:
            #         for paths in current_path:
            #             if type(paths.value) == LinkedList:
            #                 path_print.append(paths.value.get_head_node().value)
            #             else:
            #                 path_print.append(paths.value)

            #         return path_print, current_node.name, current_node.get_value()
    
                
    return None



def linear_search(current_node, current_path, goal_value):
    path_print = []
    print(f'Entering linked list {current_node.value.get_head_node().get_value()}')
    current_node = current_node.value.get_head_node()
    while current_node.get_next_node():
        current_node = current_node.get_next_node()
        if current_node.name == goal_value:
            for paths in current_path:
                if type(paths.value) == LinkedList:
                    path_print.append(paths.value.get_head_node().value)
                else:
                    path_print.append(paths.value)

            return path_print, current_node.name, current_node.get_value()
    return None