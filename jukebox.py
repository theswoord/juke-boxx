import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import random

DEVICE_ID=''
CLIENT_ID=''
CLIENT_SECRET=''

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8888/callback",
                                                scope="user-read-playback-state,user-modify-playback-state"))



# playlist_id = rfid.text #hna ghadi iji playlist dial card
playlistdata = "https://api.spotify.com/v1/playlists/{playlist_id}"


def extract_tracks(playlist_link):

    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
    return track_uris

total = extract_tracks(playlistdata)

# print(len(total))
# Transfer playback to my device if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
# Shuffle the playlist
random.shuffle(total)


# Play the spotify track at URI with ID the first song of the Playlist
sp.start_playback(device_id=DEVICE_ID, uris=[total[0]])

# Add the whole Shuffled PLaylist , khasni n7yed total[0] 7it it's already playing
for i in range(len(total)):
    sleep(0.2)
    sp.add_to_queue(total[i],DEVICE_ID)

# https://open.spotify.com/track/2mFnxVS2wZpqntPzZB17O1?si=9ceede60f7f04c79
#https://open.spotify.com/track/4TAMLjlCpo4oDLQGEFG1Znhttps://open.spotify.com/track/4TAMLjlCpo4oDLQGEFG1Zn?si=f1313db06192491?si=f1313db06192491e
# https://open.spotify.com/playlist/7xE923XvxfxFWfLfjvhMm8?si=4ea960cc8577475b