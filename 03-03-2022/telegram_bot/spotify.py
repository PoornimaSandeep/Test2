import json
import spotipy
import webbrowser


username = '31wsypv6lahzawpipv27mqf5stcm'
clientID = '344dd224b4f64125a412d8ff55bd1a5c'
clientSecret = '80226db100724fb19204dc23404fcea2'
redirectURI = 'http://google.com/'

oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user = spotifyObject.current_user()
# To print the response in readable format.
print(json.dumps(user,sort_keys=True, indent=4))

while True:
    print("Welcome, "+ user['display_name'])
    print("0 - Exit")
    print("1 - Search for a Song")
    choice = int(input("Your Choice: "))
    if choice == 1:
        # Get the Song Name.
        searchQuery = input("Enter Song Name: ")
        # Search for the Song.
        searchResults = spotifyObject.search(searchQuery,1,0,"track")
        # Get required data from JSON response.
        tracks_dict = searchResults['tracks']
        tracks_items = tracks_dict['items']
        song = tracks_items[0]['external_urls']['spotify']
        # Open the Song in Web Browser
        webbrowser.open(song)
        print('Song has opened in your browser.')
    elif choice == 0:
        break
    else:
        print("Enter valid choice.")
