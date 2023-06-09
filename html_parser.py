from bs4 import BeautifulSoup

handle = open('VideoGameRecomendtionSoftware2.html')
html = handle.read()


soup = BeautifulSoup(html, 'html.parser')
tags = soup.body.find_all('li')
video_game_data = {}
video_game_subgenres = []
video_game_flavors = []
video_game_prices = []
video_game_reviews = []

for line in tags:
    # print(line)
    if line.attrs['class'][0] == 'c6':
        main_genre = line.string
    
    if line.attrs['class'][0] == 'c5':
        sub_genre = line.string
        video_game_subgenres.append(sub_genre)

    
    if line.attrs['class'][0] == 'c1':
        video_game_name = line.string

    
    if line.attrs['class'][0] == 'c4':
        placement = line.string
        if placement == 'All flavor tags':
            placement = 0
        elif placement == 'Price':
            placement = 1
        elif placement == 'Review':
            placement = 2
        else:
            placement = 3
    
    if line.attrs['class'][0] == 'c0':
        data = line.string
        if data == None:
            data = line.get_text()
        if video_game_data.get(video_game_name) is None:
            video_game_data[video_game_name] = [main_genre, [sub_genre, []]]
        if placement == 0:
            flavors = data.split(',')
            data = []
            for flavor in flavors:
                data.append(flavor.strip())
                flavor = flavor.lower().strip()
                if flavor not in video_game_flavors:
                    video_game_flavors.append(flavor)
        elif placement == 1:
            data = data.strip()
            if data not in video_game_prices:
                video_game_prices.append(data)
        elif placement == 2:
            if not data.startswith('tbd'):
                data = data.strip()[0]
            if data not in video_game_reviews:
                
                video_game_reviews.append(data)


        video_game_data[video_game_name][1][1].append(data) 





    
