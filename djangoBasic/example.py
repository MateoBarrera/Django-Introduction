tracks = list()
tracks_uri = list()
tracks_name = list()

for track in sp.playlist_tracks(playlist_URI, limit=10)["items"]:
    
    tracks.append(track)
    #URI
    tracks_uri.append(track["track"]["uri"])

    #Track name
    tracks_name.append(track["track"]["name"])


######################################################

generos_array = np.asarray(list())
for col in lista_generos.columns:
  generos_array = np.concatenate((generos_array, top[col].unique()), axis=None)
