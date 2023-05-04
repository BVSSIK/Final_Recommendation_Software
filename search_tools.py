from collections import deque
from linked_list import LinkedList, video_game_flatten
from tree import TreeNode
from html_parser import video_game_flavors, video_game_prices, video_game_reviews
import re


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



def tag_setup(tag_type, first_phrase):

    if tag_type == 0:
        tag_list = video_game_flavors
    elif tag_type == 1:
        tag_list = video_game_prices
        print(f'Here is a list of all the prices we have in our system. Please pick from one.\n{tag_list}\n')
    elif tag_type == 2:
        tag_list = video_game_reviews
    else:
        print("Error, incorrect tag type entered")

    flavor_choices = []
    while not flavor_choices:
        starter_input = input(first_phrase) 
        for flavor in tag_list:
            if starter_input.lower() in flavor.lower():
                flavor_choices.append(flavor)
        if not flavor_choices:
            print(f"So sorry, the phrase or number you entered isn't contained in the tag list. Here is the list to help you with your choice {tag_list}\n")
            continue

    first_flavor_tag = None
    while not first_flavor_tag:
        if tag_type != 2:
            first_tag = input(f'\nThese are the choices that matched your phrase {starter_input}; {", ".join(str(e) for e in flavor_choices)}; Please fully type out the tag you would like.\n')
        else:
            first_tag = starter_input
        for flavor in flavor_choices:
            if first_tag.lower() in flavor.lower():
                first_flavor_tag = flavor
                return [tag_type, first_flavor_tag]
        print("\nSorry what you have entered doesn't match any of our flavor tags. Please try again, spelling matters.\n")
        continue


def yes_and_no(question):
    another_tag = None
    while True:
        another_tag = input(f'\n{question}\n')
        if bool(re.search('[Yy].*', another_tag)):
            return "continue"
        elif bool(re.search('[Nn].*', another_tag)):
            return "break"
        else:
            print("Enter in Y for yes and N for no")
            continue
            