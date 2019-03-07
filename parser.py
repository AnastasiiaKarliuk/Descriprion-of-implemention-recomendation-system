import requests
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import pandas as pd
import operator


id_spotify = '21681c4c54bf40e884ce470dd6136f77'
Secret_spotify = '4223065a9d5c4ab0a6fe348db1a309ee'
client_id = id_spotify
client_secret = Secret_spotify


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

    start_listeners = data.find('Monthly Listeners: ')
    end_listeners = data.find(", Where People Listen")
    listeners = data[start_listeners + 19:end_listeners]

    start_name = data.find('<title>')  # 114
    end_name = data.find(" on Spotify")
    name = data[start_name + 7:end_name]

    related_list = find_related(data)
    return name, int(listeners), related_list


def avg_listeners(name, listen_in_month):
    search_str = sys.argv[1] if len(sys.argv) > 1 else name

    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    result = sp.search(search_str)

    alboms = result['tracks']['items']
    d = {i['album']['name']: [i['album']['total_tracks'], i['album']['release_date']] for i in alboms}

    df = pd.DataFrame.from_dict(d, orient='index', columns=['Songs', 'Release Date'])
    # print(df, '\n\nTotal songs - {}\nAvg list on song - {}\n'.format(sum(df.iloc[:, 0]),
    #       listen_in_month / sum(df.iloc[:, 0])))
    return name, listen_in_month / sum(df.iloc[:, 0])


urls = ['https://open.spotify.com/artist/6LqNN22kT3074XbTVUrhzX',
        'https://open.spotify.com/artist/0C8ZW7ezQVs4URX5aX7Kqx',
        'https://open.spotify.com/artist/6wPhSqRtPu1UhRCDX5yaDJ',
        'https://open.spotify.com/artist/26dSoYclwsYLMAKD3tpOr4',
        'https://open.spotify.com/artist/0p4nmQO2msCgU4IF37Wi3j',
        "https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR",
        "https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q",
        "https://open.spotify.com/artist/3q7HBObVc0L8jNeTe5Gofh",
        'https://open.spotify.com/artist/04gDigrS5kc9YWfZHwBETP',
        'https://open.spotify.com/artist/0RqtSIYZmd4fiBKVFqyIqD',
        'https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI',
        'https://open.spotify.com/artist/1KCSPY1glIKqW2TotWuXOR',
        'https://open.spotify.com/artist/1HGTHrRQkw0BtevSo1jucU',
        'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY',
        'https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2',
        'https://open.spotify.com/artist/6jJ0s89eD6GaHleKKya26X']


names = {}
for url in urls:
    name, listen_month, artists = spotify_listeners(url)
    name, liste = avg_listeners(name, listen_month)
    names[name] = liste
    # print("{0} - {1} \n {2}\n".format(name, listen_month, str(artists)))

print(pd.DataFrame(sorted(names.items(), key=lambda kv: kv[1], reverse=True),
                   columns=['Artist', 'Avg listening on one song']))
