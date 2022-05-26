#!/usr/bin/env python3

import requests
import os
import time
import json
import spotipy
import spotipy.util as util

USERNAME = ""  # Put your Spotify username here
CLIEND_ID = ""  # Here your Client ID
CLIENT_SECRET = ""  # And client secret
REDIRECT_URI = "http://127.0.0.1/callback"  # If you follow my tutorial you can leave this

TRUNCATE = 90  # Select the amount of letters to be shown.
DELAY = 0.8  # Set delay of script (Automatically subtracts Spotify's API response time)

# ( You can probably leave this things )
LYRICS_API = "https://api.textyl.co/api/lyrics?q="
TEMP_FILE = "/tmp/.song.json"


def get_song_info():
    """
    Get information for the current playing song.
    Format:
    {
        "progress": <Progress of song in seconds>
        "query": <Song name> - <Artist>
        "id": <Spotify song ID>
    }

    Will also wait one second - API Response time.
    """
    time_before = time.time()
    scope = "user-read-currently-playing"

    token = spotipy.util.prompt_for_user_token(
        USERNAME,
        scope,
        redirect_uri="http://127.0.0.1/callback",
        client_id=CLIEND_ID,
        client_secret=CLIENT_SECRET,
    )

    if token:
        sp = spotipy.Spotify(auth=token)
        response = sp.currently_playing()

    else:
        print("Can't get token for", USERNAME)

    artist = response["item"]["album"]["artists"][0]["name"]
    track_name = response["item"]["name"]

    if time.time() - time_before <= DELAY:
        time.sleep(DELAY - (time.time() - time_before))

    return {
        "progress": response["progress_ms"] / 1000,
        "query": f"{track_name} - {artist}",
        "id": response["item"]["id"],
    }


def get_lyrics_json(query):
    """Gets the JSON response from the lyrics API"""
    try:
        return requests.get(f"{LYRICS_API}{query}").json()
    except Exception:
        return [{"seconds": 0, "lyrics": ""}]


def write_info(songid, lyrics):
    """Writes information to the TEMP_FILE so it doesnt need to get re-fetched every second"""
    with open(TEMP_FILE, "w") as f:
        f.write(json.dumps({"id": songid, "lyrics": lyrics}, indent=4))


def convert_json(lyrics):
    """
    Converts the format of the API:
    [
        "second": <n>,
        "lyrics": <text>
    ]
    to:
    <n>: <text>"""
    converted = {}
    for data in lyrics:
        converted[str(data["seconds"])] = data["lyrics"]
    return converted


def truncate(trun, text):
    """Truncates text to selected amount and appends '..'"""
    if len(text) >= trun:
        text = text[0 : trun - 2] + ".."
    return text


def get_lyrics_line():
    """Get upcoming line in lyrics"""
    song_info = get_song_info()

    lyrics = None
    if not os.path.isfile(TEMP_FILE):
        lyrics = convert_json(get_lyrics_json(song_info["query"]))
        write_info(song_info["id"], lyrics)
    else:
        with open(TEMP_FILE, "r") as f:
            if json.loads(f.read())["id"] != song_info["id"]:
                lyrics = convert_json(get_lyrics_json(song_info["query"]))
                write_info(song_info["id"], lyrics)
    if lyrics == None:
        with open(TEMP_FILE, "r") as f:
            lyrics = json.loads(f.read())["lyrics"]
    else:
        lyrics = lyrics

    curr_second = song_info["progress"]
    keys_as_int = [int(x) for x in list(lyrics.keys())]
    
    
    if len(lyrics) == 1 and lyrics[0] == "":
        print("")
    elif int(round(song_info["progress"])) in keys_as_int:
        print(truncate(TRUNCATE, lyrics[str(round(song_info["progress"]))]))
    elif int(round(song_info["progress"])) <= keys_as_int[0]:
        print(".. " + lyrics[str(keys_as_int[0])])


try:
    get_lyrics_line()
except Exception:
    print("")
