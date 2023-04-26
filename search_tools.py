from collections import deque
from linked_list import LinkedList, video_game_flatten
from tree import TreeNode


def bfs(root_node, goal_value, child_report=False, parent_report=False):

    path_queue = deque()

    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        print(f'Searching node with value: {current_node.value}')

        if current_node.value == goal_value and child_report == False and parent_report == False:
            return current_path
        elif current_node.value == goal_value and parent_report == False:
            return current_node.children
        elif current_node.value == goal_value:
            return current_node.children, current_node


        for child in current_node.children:
            new_path = current_path.copy()
            new_path.append(child)
            path_queue.appendleft(new_path)
        
        if type(current_node.value) == LinkedList:
            print(f'{current_node.value.get_head_node().get_value()} - {goal_value}')
            if current_node.value.get_head_node().get_value() == goal_value:
                return video_game_flatten(current_node.value, False)
     
    return None


def node_list_value_printer(nodes):
    lst_version = []
    for node in nodes:
        if type(node) == TreeNode and type(node.value) != LinkedList:
            lst_version.append(node.value) 
        elif type(node.value) == LinkedList:
            lst_version.append(node.value.get_head_node().get_value())
        elif type(node) == LinkedList:
            lst_version.append(node.get_head_node().get_value())
    return lst_version

