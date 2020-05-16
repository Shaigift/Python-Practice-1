def make_album(artist_name, album_name):
    """Return album name and artist name"""
    artist_info = {'artist': artist_name, 'album': album_name}
    return artist_info

while True:
    print("\nPlease enter artist name & album name:")
    print("(enter 'q' at any time to quit)")
    first_name = input("First name: ")
    if first_name == 'q':
        break

    album_name = input("Album: ")
    if first_name == 'q':
        break
        
    album = make_album(first_name, album_name)
    print(f"\n Hello , this is the artist information {album}")
