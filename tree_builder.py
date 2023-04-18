from linked_list import Node, LinkedList
from tree import TreeNode
from search_tools import dfs, bfs, node_list_value_printer
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


bfs_search = bfs(video_game_tree_root, 'MMORPG')
dfs_search = dfs(video_game_tree_root, 'MMORPG', True)

print(bfs_search)
print(dfs_search)

#node_list_value_printer(bfs_search)
#node_list_value_printer(dfs_search)

# for ans in bfs_search:
#     if type(ans.value) == LinkedList:
#         print(ans.value.get_head_node().get_value())
    #print(ans)

# dfs_search = dfs(video_game_tree_root, 'World of Warcraft')
# for ans in dfs_search:
#     if type(ans) == TreeNode:
#         print(ans.value)
#     print(ans)


# dr = video_game_tree_root.depth_report(1)
# # print(dr)
# if dr != None:
#     for node in dr:
#         if type(node.value) == LinkedList:
#             print(f'report - {node.value.get_head_node().value}')
#         else:
#             print(f'report - {node.value}')