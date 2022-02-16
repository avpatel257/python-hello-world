class Track:
    def __init__(self, id, title, artist):
        self.id = id
        self.title = title
        self.artist = artist

def get_tracks():
    tracks = []
    for i in range(10):
        track = Track(1, 'Bad Romance', 'Lady Gaga')
        tracks.append(track)
    return tracks