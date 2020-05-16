def make_album(artist_name, album_name, song_number=None):
    """Return album name and artist name"""
    artist_info = {'artist': artist_name, 'album': album_name}
    if song_number:
        artist_info['song_number'] = song_number
    return artist_info
artist = make_album('Kendrick Lamar', 'To Pimp A Butterfly', song_number=15)
print(artist)


def make_album(artist_name, album_name, song_number=None):
    """Return album name and artist name"""
    artist_info = {'artist': artist_name, 'album': album_name}
    if song_number:
        artist_info['song_number'] = song_number
        return artist_info
artist = make_album('J. Cole', 'Cole World', song_number= 17)
print(artist)



def make_album(artist_name, album_name, song_number=None):
    """Return album name and artist name"""
    artist_info = {'artist': artist_name, 'album': album_name}
    if song_number:
        artist_info['song_number'] = song_number
        return artist_info
artist = make_album("Clearwater Credence", "'Cosmo's Factory", song_number= 12)
print(artist)