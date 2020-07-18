# paylist title
#   creator
#       song
#           title
#           artist
#           album
#       song
#           title
#           artist
#           album


playlist = {
    'pl_name': "Tyler's playlist",
    'created_by': 'Tyler',
    'songs': [
        {
            'title': 'Fast Car',
            'artist': ['Tracy Chapman'],
            'album': 'Greatest Hits'
        },
        {
            'title': 'Girl From the North Country',
            'artist': ['Bob Dylan', 'Johnny Cash'],
            'album': 'Nashville Skyline'
        },
        {
            'title': 'Wildflowers',
            'artist': ['Tom Petty'],
            'album': 'Wildflowers'
        }
    ],
}

song_list = ''
song_count = 0
playlist_name = playlist.get('pl_name')
for song in playlist['songs']:
    s = song.get('title')
    song_list += s + ', '
    song_count += 1
print(f'{playlist_name} has {song_count} songs: {song_list}')
