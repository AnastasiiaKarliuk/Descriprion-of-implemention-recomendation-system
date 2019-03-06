import requests


def find_related(data, s1=0):
    related_list = []
    for i in range(4):
        s = data.find('&quot;//i.scdn.co/image', s1)
        s1 = data.find('</span>', s)
        related_list.append(data[s + 102:s1])
    return related_list


def spotify_listeners(url):
    htmlContent = requests.get(url, verify=False)
    data = htmlContent.text

    print(data)


    start_listeners = data.find('Monthly Listeners: ')
    end_listeners = data.find(", Where People Listen")
    listeners = data[start_listeners + 19:end_listeners]

    start_name = data.find('<title>')  # 114
    end_name = data.find(" on Spotify")
    name = data[start_name + 7:end_name]

    related_list = find_related(data)
    return name, int(listeners), related_list


urls = ["https://open.spotify.com/artist/0RqtSIYZmd4fiBKVFqyIqD",
        "https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR",
        "https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q",
        "https://open.spotify.com/artist/3q7HBObVc0L8jNeTe5Gofh",
        'https://open.spotify.com/artist/04gDigrS5kc9YWfZHwBETP',
        'https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI']


for url in urls:
    name, listen, artists = spotify_listeners(url)
    print("{0} - {1} \n {2}\n\n".format(name, listen, str(artists)))



# import sys
# from spotipy.oauth2 import SpotifyClientCredentials
# import spotipy
# import pprint
#
# id_spotify = '21681c4c54bf40e884ce470dd6136f77'
# Secret_spotify = '4223065a9d5c4ab0a6fe348db1a309ee'
#
# if len(sys.argv) > 1:
#     search_str = sys.argv[1]
# else:
#     search_str = 'ariana grande'
#
# client_id = id_spotify
# client_secret = Secret_spotify
#
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# result = sp.search(search_str)
# pprint.pprint(result)