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
        #         if type(current_node.value) == LinkedList:
        #             video_game_linked = current_node.value.get_head_node()
        #             while video_game_linked:
        #                 if video_game_linked.name != None and tag in video_game_linked.value[0]:
        #                     # print(video_game_linked.get_value())
        #                     # print(video_game_linked.name)
        #                     video_games_to_print.insert_beginning(video_game_linked.get_value(), video_game_linked.name)

        #                 video_game_linked = video_game_linked.get_next_node()

        #     nodes_to_visit += current_node.children
        # return video_games_to_print
    
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



# def tag_search(current_node, tag): 
#     #print(current_node)
#     video_games_to_print = None
#     if type(current_node.value) == LinkedList:
#         video_games_to_print = LinkedList()
#         video_game_linked = current_node.value.get_head_node()
#         while video_game_linked:
#             if video_game_linked.name != None and tag in video_game_linked.value[0]:
#                 # print(video_game_linked.get_value())
#                 # print(video_game_linked.name)
#                 video_games_to_print.insert_beginning(video_game_linked.get_value(), video_game_linked.name)

#             video_game_linked = video_game_linked.get_next_node()

#         #print(video_game_flatten(video_games_to_print, False))
#     return video_games_to_print