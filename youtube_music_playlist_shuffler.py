pip install ytmusicapi

from ytmusicapi import YTMusic
from random import shuffle

headers = YTMusic.setup(filepath="headers_auth.json", headers_raw = """GET /getDatasyncIdsEndpoint HTTP/1.1
Host: music.youtube.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Goog-Visitor-Id: CgswSE10MVpnY0Q3dyiExsGTBg%3D%3D
X-Youtube-Client-Name: 67
X-Youtube-Client-Version: 1.20220427.01.00
X-Goog-AuthUser: 0
X-Origin: https://music.youtube.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
Authorization: SAPISIDHASH 1651532550_e83cce0d19a18fe80d70b32af9910d2e7b596186
Referer: https://music.youtube.com/
Alt-Used: music.youtube.com
Connection: keep-alive
Cookie: VISITOR_INFO1_LIVE=0HMt1ZgcD7w; PREF=volume=100&library_tab_browse_id=FEmusic_liked_playlists&f4=4000000&f5=30000&tz=America.New_York&f6=40000400; SID=JQj1WKAWoe_PWHImgroWshYnJflGWurI1pjGsW8IeRRBZ77QCFtXHD2iZBeY3MLWL8G1Lg.; __Secure-1PSID=JQj1WKAWoe_PWHImgroWshYnJflGWurI1pjGsW8IeRRBZ77QjPo--8g1v8UEMjV5huYYPA.; __Secure-3PSID=JQj1WKAWoe_PWHImgroWshYnJflGWurI1pjGsW8IeRRBZ77Q8HzjypPz88akru2thA7szQ.; HSID=ASSoL7dt0y25CEQ3A; SSID=Ap-Xe1PZFu8FrB3ic; APISID=Poyit_cnuj8YxXk9/AlEz6L6QKB0SRP-TI; SAPISID=lqEq1fRNz29qLZIk/AoQGYaR5rmHj0yhkn; __Secure-1PAPISID=lqEq1fRNz29qLZIk/AoQGYaR5rmHj0yhkn; __Secure-3PAPISID=lqEq1fRNz29qLZIk/AoQGYaR5rmHj0yhkn; LOGIN_INFO=AFmmF2swRgIhALqZzXxGmHhKvUhU2VPxO8zFevFH9W0As5C0fftY5NyNAiEAo3sPNr3IvKrUjbpz9aaaqQdLUGHjdcIms6YKKDOOhhw:QUQ3MjNmeHJOUmd6RXBWY2ZzMzF6Y0dlQ2lncHdQU2J2dWtTa05MSEJSMEZJZU4wM3N5QUplbHpsTGZITDNIT19FdFpTemU2Rm1yZ0tuT3dVTnNmTXJYTjd6SUhTZnlsNXRqOFpsT0hjTEk1OHp6MnRzMGYwb0I1dG55a1p3cjBMNktfQnZHMmJCdlRsVS1tOEhRbzFfR1VlYVA1bXdSZUpB; SIDCC=AJi4QfH3t_iYo3Q6cKF5A5IirHwgAAolfAXk2naKETMT3B9oytXRk4CdTI8HB57NddYg8PkTHw; __Secure-3PSIDCC=AJi4QfGEKC1N5Yr51Vvv6yYQaHs0KrRX6SeBD5xkjPYlx7tfu3mOFB9b503LPhV8GhHFY22ludw; YSC=w-D6rA_Nu00
Cache-Control: max-age=0""")
ytmusic = YTMusic("headers_auth.json")

# The above lines run the youtube nusic setup and authenticate it. For information on what is happening or how to coppy the cookie needed (valid for about 2 years) plase see the youtube music documentation: https://ytmusicapi.readthedocs.io/en/latest/reference.html#library

# The lines below are the meat of the program

#Playlist titles

#"TestPlaylist"
#"pagan bops"
#"Fogbanks Over Celtic Highlands"
#"O'dark thirty vibes before skiing"
#"Yuletide"
#"Sapphic Sunsets"
#"Chill vibes"
#"Songs for Storming Castles"
#"Chillstep to work to"
#"Dance Music"
#"league esque songs"
#"Feeeeelings"
#"Spoon stealing"
#"Murder Vintage Swing"
#"Working songs and shanties to start the revolution"
#"Stims to remind who you are"

#please put the title of the playlist in the string
playlistToShuffle = "Chillstep to work to"

"""If you update the cell above then run the whole notebook this should shuffle your playlist for you.

This cell creates some helper functions for sub parts of the process
"""

def getPlaylistFromTitle(searchTitle, playlists):
  #a function that searches your library for a specific playlist and returns it
  for plist in playlists:
    if plist["title"] == searchTitle:
      return plist

def getTracks (id,numOfTracks=5000):
  #a function that gets the reacks from a playlist if you pass it the id of the playlist
  return ytmusic.get_playlist(id,numOfTracks)['tracks']

def getTrackVideoIds(tracks):
  #a function that extracts the videoIds from a list of tracks
  videoIdList = []
  for track in tracks:
    videoIdList.append(track['videoId'])
  return videoIdList

def reorderPlaylist(id,orderedTrackIdList):
  #this function orders the playlist into the order supplied the the provided track list

  #core algorithm is a sift to front.move the track that is before the lst to be before it... move the track in front of that one to be in front of it. so on so forth untill al of the tracks have been moved to their place except for the last track which was not moved but sifted to the end naturally
  indexFromEnd = -2
  while -1* indexFromEnd <= len(orderedTrackIdList):
    #generate the pair that needs to be moved. in the form of (song to move, infront of this song)
    movementTuple = (orderedTrackIdList[indexFromEnd],orderedTrackIdList[indexFromEnd+1])

    #perform the switch
    ytmusic.edit_playlist(id,moveItem=movementTuple)

    #incremant the index
    indexFromEnd -= 1

def shufflePlaylist(playlistTitle):
  #a function that shuffles a playlist
  #retrieve playlists from the server
  playlists = ytmusic.get_library_playlists(1)
  #get playlist
  plist = getPlaylistFromTitle(playlistTitle,playlists)
  #get the tracks in the playlist
  tracks = getTracks(plist['playlistId'])
  #get the videoIds of the tracks (the id of theri specific youtube video)
  trackVideoIds = getTrackVideoIds(tracks)
  #randomize the order of the tracks
  shuffle(trackVideoIds)

  if 'description' in plist:
    description = plist['description']
  else:
    description = ""
  
  #rename the old playlist
  ytmusic.edit_playlist(plist['playlistId'],title = "#")
  #make the new playlist
  ytmusic.create_playlist(plist['title'],description,video_ids=trackVideoIds)

  #delete the old playlist after we made the new one
  ytmusic.delete_playlist(plist["playlistId"])

def removeDuplicates(playlistTitle):
  #a function that removes duplicate songs from a specified playlist
  #retrieve playlists from the server
  playlists = ytmusic.get_library_playlists(1)
  #get playlist
  plist = getPlaylistFromTitle(playlistTitle,playlists)
  #get the tracks in the playlist
  tracks = getTracks(plist['playlistId'])
  #get the videoIds of the tracks (the id of theri specific youtube video)
  trackVideoIds = list(dict.fromkeys(getTrackVideoIds(tracks)))

  if 'description' in plist:
    description = plist['description']
  else:
    description = ""
  
  #delete the old playlist
  ytmusic.delete_playlist(plist["playlistId"])
  #make the new playlist
  ytmusic.create_playlist(plist['title'],description,video_ids=trackVideoIds)

#shuffle the designated playlist
#shufflePlaylist(playlistToShuffle)

regularShuffles = ["Working songs and shanties to start the revolution","Fogbanks Over Celtic Highlands","Songs for Storming Castles","Chill vibes", "Spoon Stealing"]
for plst in regularShuffles:
  shufflePlaylist(plst)