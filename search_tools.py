from collections import deque
from linked_list import LinkedList
from tree import TreeNode


def dfs(root, target, child_report = False, path=()):
    path = path + (root,)

    if root.value == target and child_report == False:
        return path
    elif root.value == target and child_report == True:
        return root.children

    if type(root.value) == LinkedList:
        linked_list_check = linear_search(root, path, target)
        if linked_list_check != None:
            if child_report == True:
                    return root.value.video_game_flatten()
            return linked_list_check


    
    for child in root.children:
        path_found = dfs(child,target,child_report, path)

        if path_found is not None:
            return path_found
        
    return None


def bfs(root_node, goal_value, child_report=False):

    path_queue = deque()

    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f'Searching node with value: {current_node.value}')

        if current_node.value == goal_value and child_report == False:
            return current_path
        elif current_node.value == goal_value:
            return current_node.children


        for child in current_node.children:
            new_path = current_path.copy()
            new_path.append(child)
            path_queue.appendleft(new_path)
        
        if type(current_node.value) == LinkedList:
            linked_list_check = linear_search(current_node, current_path, goal_value)
            if linked_list_check != None:
                if child_report == True:
                    return current_node.value.video_game_flatten()
                return linked_list_check
     
    return None



def linear_search(current_node, current_path, goal_value):
    path_print = []
    print(f'Entering linked list {current_node.value.get_head_node().get_value()}')
    current_node = current_node.value.get_head_node()
    while True:
        # current_node = current_node.get_next_node()
        if current_node.name == goal_value or current_node.value == goal_value:
            for paths in current_path:
                if type(paths.value) == LinkedList:
                    path_print.append(paths.value.get_head_node().value)
                else:
                    path_print.append(paths.value)
            return path_print, current_node.name, current_node.get_value()
        
        if current_node.get_next_node() == None:
            break
        current_node = current_node.get_next_node()
    return None


def node_list_value_printer(nodes):
    for node in nodes:
        if type(node) == TreeNode and type(node.value) != LinkedList:
            print(node.value)
        elif type(node.value) == LinkedList:
            print(node.value.get_head_node().get_value())
        elif type(node) == LinkedList:
            print(node.get_head_node().get_value())


