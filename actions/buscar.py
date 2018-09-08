import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyBusca():

    def buscar_playlist(self, playlistUrl ):
        # Ok, i know that is a mistake to put my credentials here
        # but I'd rather believe in humanity
        client_credentials_manager = SpotifyClientCredentials(client_id='8c337c38f249400d8e08ea68a19cc153',client_secret='70e22673325743ba8b1ae5ad8f283b16')
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        parts     = playlistUrl.split( ':' ) #spotify:user:12142725670:playlist:2LaVlt7pjRAPBv9Ccbeh75
        playlists = sp.user_playlist(user=parts[2], playlist_id=parts[4])

        tracks    = playlists['tracks']

        return_tracks = []

        for i, item in enumerate(tracks['items']):
            track = item['track']
            return_tracks.append(
                [i, track['artists'][0]['name'], track['name'], track['id'], '', '']
            )
        
        return return_tracks

