from bs4 import BeautifulSoup

handle = open('VideoGameRecomendtionSoftware2.html')
html = handle.read()


soup = BeautifulSoup(html, 'html.parser')
# tags = soup.body.find_all('li')
tags = soup.body.find_all('li')
video_game_data = {}
video_game_subgenres = []
video_game_flavors = []

for line in tags:
    #print(line)
    if line.attrs['class'][0] == 'c8':
        main_genre = line.string
        #print(main_genre)
    
    if line.attrs['class'][0] == 'c5':
        sub_genre = line.string
        #print(sub_genre)
        video_game_subgenres.append(sub_genre)

    
    if line.attrs['class'][0] == 'c3':
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


        video_game_data[video_game_name][1][1].append(data) 

    

    

#print(video_game_data['New World'])
#print(video_game_subgenres)
print(video_game_flavors)
