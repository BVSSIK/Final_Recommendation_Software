from linked_list import Node, LinkedList
from tree import TreeNode
from search_tools import bfs, node_list_value_printer
from html_parser import video_game_data, video_game_subgenres

def tree_builder(video_game_data, video_game_subgenres):

    # Creating the main tree to hold all the different video game genres
    video_game_tree_root = TreeNode('Genres')

    #Creating the genre trees to hold all the subgenres for the games
    adventure = TreeNode('Adventure')
    video_game_tree_root.add_child(adventure)
    rpg = TreeNode('RPG')
    video_game_tree_root.add_child(rpg)
    strategy = TreeNode('Strategy')
    video_game_tree_root.add_child(strategy)
    sports = TreeNode('Sports')
    video_game_tree_root.add_child(sports)


    #Creating the sub-genre linked-lists to hold 
    for subgenre in video_game_subgenres:
        ordered_list = LinkedList(f'{subgenre}')
        for k, v in video_game_data.items():
            if v[1][0] == subgenre:
                ordered_list.insert_end(v[1][1], k)
        ordered_tree = TreeNode(ordered_list)
        if ordered_list.get_head_node().get_value() in ['Platformer', 'Shooter', 'Survival']:
            adventure.add_child(ordered_tree)
        elif ordered_list.get_head_node().get_value() in ['Story-Driven RPG', 'ARPG (Diablo-Like)', 'MMORPG', 'Turn-Based RPGs']:
            rpg.add_child(ordered_tree)
        elif ordered_list.get_head_node().get_value() in ['RTS', 'MOBA', 'City-Building']:
            strategy.add_child(ordered_tree)
        elif ordered_list.get_head_node().get_value() in ['Fighting', 'Racing', 'Team Sports']:
            sports.add_child(ordered_tree)
    return video_game_tree_root


