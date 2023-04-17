from linked_list import Node, LinkedList
from tree import TreeNode
from search_tools import dfs, bfs
from html_parser import video_game_data, video_game_subgenres

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
    #print(ordered_list.stringify_list())
    ordered_tree = TreeNode(ordered_list)
    if ordered_list.get_head_node().get_value() in ['Platformer', 'Shooter', 'Survival']:
        #print(f'I am an adventure game: {ordered_list.get_head_node().get_value()}')
        adventure.add_child(ordered_tree)
    elif ordered_list.get_head_node().get_value() in ['Story-Driven RPG', 'ARPG (Diablo-Like)', 'MMORPG', 'Turn-Based RPGs']:
        #print(f'I am a RPG game: {ordered_list.get_head_node().get_value()}')
        rpg.add_child(ordered_tree)
    elif ordered_list.get_head_node().get_value() in ['RTS', 'MOBA', 'City-Building']:
        #print(f'I am a Strategy game: {ordered_list.get_head_node().get_value()}')
        strategy.add_child(ordered_tree)
    elif ordered_list.get_head_node().get_value() in ['Fighting', 'Racing', 'Team Sports']:
        # print(f'I am a Sports game: {ordered_list.get_head_node().get_value()}')
        sports.add_child(ordered_tree)

video_game_tree_root.traverse()

search = bfs(video_game_tree_root, 'Trackmania')

for ans in search:
    if type(ans) == TreeNode:
        print(ans.value)
    print(ans)


