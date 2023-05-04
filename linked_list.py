class Node:
    def __init__(self, value, name=None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.name = name

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value, name=None):
        new_node = Node(new_value, name)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, new_value, name=None):
        new_node = Node(new_value, name)
        last_node = self.head_node
        while True:
            if last_node.get_next_node() == None:
                last_node.set_next_node(new_node)
                break
            else:
                last_node = last_node.get_next_node()

    def combine(self, new_lst):
        current_node = new_lst.get_head_node()
        while current_node.get_value():
            self.insert_beginning(current_node.get_value(), current_node.name)
            current_node = current_node.get_next_node()
        return self


    def stringify_list(self):
        list_info = ""
        sequence = self.head_node

        while sequence:
            if sequence.get_value() != None:
                if sequence.name == None:
                    list_info += str(sequence.get_value()) + '\n'
                elif sequence.name != None:
                    list_info += str(sequence.name) + ' - ' + str(sequence.get_value()) + '\n'
                sequence = sequence.get_next_node()
        return list_info
    

    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if self.head_node.get_value() == value_to_remove:
            self.head_node = self.head_node.get_next_node()
        else:
            while current_node:
                current_next_node = current_node.get_next_node()
                if current_next_node.get_value() == value_to_remove:
                    current_node.set_next_node(current_next_node.get_next_node())
                    current_node = None
                else:
                    current_node = current_next_node



def video_game_flatten(linked_list, single=True):
    list_info = ""
    if type(linked_list) == LinkedList:
        sequence = linked_list.get_head_node()
    else:
        sequence = linked_list
    while sequence:
        if sequence.get_value() != None:
            if type(sequence.get_value()) == list and sequence.name != None:
                list_info += f'{sequence.name}\n'
                for data in range(len(sequence.get_value())):
                    if data == 0:
                        list_info += f'Flavor Tags: {sequence.get_value()[data]}\n'
                    elif data == 1:
                        list_info += f'Price: {sequence.get_value()[data]}\n'
                    elif data == 2:
                        list_info += f'Rating: {sequence.get_value()[data]}\n'
                    elif data == 3:
                        list_info += f'Summary: {sequence.get_value()[data]}\n\n\n'              
            elif sequence.name == None:
                list_info += '\n' + str(sequence.get_value()) + '\n\n'
            
            if not single:
                sequence = sequence.get_next_node()
            else:
                break
        else:
            break
            
    return list_info


def tag_search(current_node, tag, search_type): 
    #types are 0 = flavor tags, 1 = Price, 2 = Review, 3 = Summary
    video_games_to_print = None
    video_game_linked = None
    if type(current_node) == LinkedList:
        video_game_linked = current_node.get_head_node()
    elif type(current_node.value) == LinkedList:
        video_game_linked = current_node.value.get_head_node()
        
    if video_game_linked:
        video_games_to_print = LinkedList()
        while video_game_linked:
            if video_game_linked.name != None and tag in video_game_linked.value[search_type]:
                video_games_to_print.insert_beginning(video_game_linked.get_value(), video_game_linked.name)

            video_game_linked = video_game_linked.get_next_node()

    return video_games_to_print