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
    
    def insert_beginning(self, new_value, name):
        new_node = Node(new_value, name)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def insert_end(self, new_value, name):
        new_node = Node(new_value, name)
        last_node = self.head_node
        while True:
            if last_node.get_next_node() == None:
                last_node.set_next_node(new_node)
                break
            else:
                last_node = last_node.get_next_node()


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
    

    def video_game_flatten(self):
        list_info = ""
        sequence = self.head_node

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