from linked_list import LinkedList, video_game_flatten, tag_search



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self,child_node):
        #print(f'Adding {child_node.value}')
        self.children.append(child_node)

    def remove_child(self, child_node):
        print(f'Removing {child_node.value} from {self.value}')
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self, tag = None, linked_list_search=True):
        print('Traversing...')
        nodes_to_visit = [self]
        nodes_to_print = LinkedList()
        while len(nodes_to_visit) != 0:
            current_node = nodes_to_visit.pop()
            if linked_list_search == False:
                print(current_node.value)
            elif tag != None:
                current_tag_matches = tag_search(current_node, tag)
                if current_tag_matches:
                    nodes_to_print.combine(current_tag_matches)
            nodes_to_visit += current_node.children
            
        return nodes_to_print

    def depth_report(self, depth):
        prev_depth = [self]
        nodes_at = []
        while prev_depth:
            current_node = prev_depth.pop(0)
            nodes_at += current_node.children
            if len(current_node.children) == 0:
                return None
                

            if depth != 0:
                prev_depth += nodes_at
                nodes_at = []
                depth -= 1     
        return nodes_at
