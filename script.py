from tree_builder import tree_builder
from html_parser import video_game_data, video_game_subgenres
from intro import intro
from search_tools import dfs, bfs
from linked_list import video_game_flatten, tag_search
import re


video_game_tree_root = tree_builder(video_game_data, video_game_subgenres)

print(intro)

while True:
    
    search_type = input('\nWelcome to the Destiny Game Machine, we have 2 different types of searches for you a "tag search" and a "genre search"\nOur "tag search" will allow you to type the start of a flavor tag of a game like "sci-fi" or "multiplayer"\nWhile our "genre search" will guide you from genre to sub-genre and then will list off all games in the chosen sub-genre\nWhat search would you like\n')
    if bool(re.search('[Tt].*',search_type)):
        print('Tag Search')
        ans = video_game_tree_root.traverse('singleplayer')
        print('Traverse Done')

        #print(video_game_flatten(ans, False))
        ans2 = tag_search(ans, 'multiplayer')
        #print(video_game_flatten(ans2, False))
        ans3 = tag_search(ans2, 'shooter')
        print(video_game_flatten(ans3))


    elif bool(re.search('[Gg],*',search_type)):
            print('Genre Search')
    else:
         print('Please choose from either "tag search" or "genre search"')
         continue
    
    
    break
