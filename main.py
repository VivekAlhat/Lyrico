import re
import json
import urllib3

# Disable all HTTP warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connection pool
http = urllib3.PoolManager()

# Getting input
artist = input("Artist: ")
artistList = re.split(r'\s|-', artist)
artist = "-".join(artistList)
title = input("Track: ")
titleList = re.split(r'\s|-', title)
title = "-".join(titleList)


def fetchLyrics(artist, title):
    url = "https://api.lyrics.ovh/v1/{}/{}".format(artist, title)
    resp = http.request('GET', url)
    apiResponse = json.loads(resp.data.decode('utf8'))
    if 'lyrics' in apiResponse.keys():
        print(apiResponse['lyrics'])
        # with open("{}.txt".format(title), "w") as lyricFile:
        #     lyricFile.write(apiResponse['lyrics'])
    else:
        print("No Lyrics Found")
    # print(type(apiResponse['lyrics']))

fetchLyrics(artist, title)
