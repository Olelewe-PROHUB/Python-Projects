#This program will create a dictionary entry for several different artists 
#In each entry will be the artists name, followed by the name of an album
#In addition to the album, there will also be an entry for the number of 
#Songs, not every function call will include an entry for the number of songs

#This new program will create a while loop that takes input

def get_album(art_name, art_bum, art_num = None):
    """Return dictionary information about an artist and their music"""
    artist = {'Name': art_name, 'Album': art_bum}
    if art_num:
        artist['Number of Songs'] = art_num
    return artist


while True:
    print("Welcome to the music library")
    print("Please enter the name of an artist and album for entry")
    print("\n")

    musician_name = input("Please Enter the Artists Name (enter 'q' to quit): ")
    if musician_name == 'q':
        break
    print("\n")
    
    musician_album = input("Please Enter the Album Name (enter 'q' to quit): ")
    if musician_album == 'q':
       break
    print("\n")
    
    entry = get_album(musician_name, musician_album)
    print(entry)
    print("\n")
