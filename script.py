from tree_builder import tree_builder
from html_parser import video_game_data, video_game_subgenres, video_game_flavors, video_game_prices, video_game_reviews
from intro import intro
from search_tools import bfs, node_list_value_printer, tag_setup
from linked_list import video_game_flatten, tag_search
import re


video_game_tree_root = tree_builder(video_game_data, video_game_subgenres)

print(intro)

while True:
    
    search_type = input('\nWelcome to the Destiny Game Machine, we have 2 different types of searches for you a "tag search" and a "genre search"\nOur "tag search" will allow you to type the start of a game tag like "sci-fi" or "multiplayer",\n its price (prices will be listed for choice when picked) or its review out of 5 like 3 or 4 \nWhile our "genre search" will guide you from genre to sub-genre and then will list off all games in the chosen sub-genre\nWhat search would you like\n')
    
    if bool(re.search('[Tt].*',search_type)):
        search_type = 'Tag Search'
        print(f"\nThank you for choosing {search_type}")
        flavor_tag_picks = []

        while True:
            what_data = input(f"What would you like your tag choice to be?\nFlavor, Price or Review out of 5\n")


            if bool(re.search('[Ff]\S*', what_data)):
                placement = 0
                is_there_something = tag_setup(placement, "Please enter the starting letters of a video game's flavor tag ex. sci for Sci-Fi or mul for multiplayer\n" )
                if is_there_something:
                    flavor_tag_picks.append(is_there_something)

            elif bool(re.search('[Pp]\S*', what_data)):
                placement = 1
                is_there_something = tag_setup(placement, "Please enter the price of game you would like to look for. (Only 1 Price tag can be entered)\n" )
                if is_there_something:
                    flavor_tag_picks.append(is_there_something)

            elif bool(re.search('[Rr]\S*', what_data)):
                placement = 2
                is_there_something = tag_setup(placement, "Please enter a number out of 5. ex 1 , 4 \n (Only 1 Review tag can be entered) ")
                if is_there_something:
                    flavor_tag_picks.append(is_there_something)
            
            else:
                print("Please enter a correct tag choice\n")
                continue


            if len(flavor_tag_picks) >= 3:
                break
            another_tag = input(f'\nWould you like to add another tag (Up to 3)? y/n\n')
            if bool(re.search('[Yy].*', another_tag)):
                continue
            else:
                break

        for final_pick in range(len(flavor_tag_picks)):
            if final_pick == 0:
                final_link = video_game_tree_root.traverse(flavor_tag_picks[final_pick][1], search_type=flavor_tag_picks[final_pick][0])
            else:
                final_link = tag_search(final_link, flavor_tag_picks[final_pick][1], search_type=flavor_tag_picks[final_pick][0] )
        response = video_game_flatten(final_link, False)
        if response:
            print(response)
        else:
            print(f"Your tag choices have resulted in no games being found, try again with less or different tags")
  


    elif bool(re.search('[Gg],*',search_type)):
            search_type = 'Genre Search'
            first_choices = video_game_tree_root.depth_report(0)
            first_choices = node_list_value_printer(first_choices)
            str_first_choices = ""
            for x in first_choices:
                str_first_choices += x + ", "

            first_pick_real = None
            while not first_pick_real:
                first_pick = input(f'\nPlease pick from the following genres; {str_first_choices}\n')
                for check in first_choices:
                    print(f'{check} - {first_pick.capitalize()}')
                    if first_pick.capitalize() == check.capitalize():
                        first_pick_real = check
                        break

                if first_pick_real == None:
                    print("\nSorry you have entered something that isn't apart of your choice. Please try again, spelling counts.\n")
                    continue
            
            pre_second_choices = bfs(video_game_tree_root, first_pick_real, True, True)
            second_choices = node_list_value_printer(pre_second_choices[0])
            str_second_choices = ""
            for x in second_choices:
                str_second_choices += x + ", "

            second_pick_real = None
            while not second_pick_real:
                second_pick = input(f'\nPlease pick from the following sub-genres; {str_second_choices}\n')
                for check in second_choices:
                    if second_pick.capitalize() == check.capitalize():
                        second_pick_real = check
                        break

                if second_pick_real == None:
                    print("\nSorry you have entered something that isn't apart of your choice. Please try again, spelling counts.\n")
                    continue
            print(bfs(pre_second_choices[1], second_pick_real, True, True))



    else:
         print('Please choose from either "tag search" or "genre search"')
         continue
    
    
    again = input(f'\nDo you want to use the Destiny Game Machine again? y/n\n')
    if bool(re.search('[Yy],*', again)):
        continue
    else:
        break



