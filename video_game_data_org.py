### This was going to be used to hold the data of the video games but I got lazy and decide to just parse the html of the doc where I already wrote all the data out, html_parser now
### holds video_game_data with all the data in it. This is just used to have a visual of the organization of the original data




video_game_data= {
    "It Takes Two" : ['Adventure', ['Platformer', [['platformer', 'co-op', 'multiplayer', '3d', 'puzzle' ], "$39.99", 5, "Embark on the craziest journey of your life in It Takes Two, a genre-bending platform adventure created purely for co-op. Invite a friend to join for free with Friend's Pass and work together across a huge variety of gleefully disruptive gameplay challenges. Play as the clashing couple Cody and May, two humans turned into dolls by a magic spell. Together, trapped in a fantastical world where the unpredictable hides around every corner, they are reluctantly challenged with saving their fractured relationship.\nMaster unique and connected character abilities in every new level. Help each other across an abundance of unexpected obstacles and laugh-out-loud moments. Kick gangster squirrels' furry tails, pilot a pair of underpants, DJ a buzzing night club, and bobsleigh through a magical snow globe. Embrace a heartfelt and hilarious story where narrative and gameplay weave into a uniquely metaphorical experience.\nIt Takes Two is developed by the award-winning studio Hazelight, the industry leader of cooperative play. They're about" ]]],
    "Crash Bandicoot Sane Trilogy" : ['Adventure', ['Platformer', [['platformer', 'singleplayer', 'co-op', '2d', 'arcade', 'retro'], '$39.99', 4, "Your favorite marsupial, Crash Bandicoot™, is back! He’s enhanced, entranced and ready-to-dance with the N. Sane Trilogy game collection. Now you can experience Crash Bandicoot like never before. Spin, jump, wump and repeat as you take on the epic challenges and adventures through the three games that started it all, Crash Bandicoot™, Crash Bandicoot™ 2: Cortex Strikes Back and Crash Bandicoot™ 3: Warped. Relive all your favorite Crash moments in their fully-remastered graphical glory and get ready to put some UMPH in your WUMP!"]]]
}


print(video_game_data['Crash Bandicoot Sane Trilogy'][1][1][3])