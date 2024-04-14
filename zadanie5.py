class Song:
    def __init__(self, title, album, artist) -> None:
        self.title = title
        self.album = album
        self.artist = artist


class Playlist:
    def __init__(self, songs=[]):
        self.songs = songs

    def __add__(self, value):
        if isinstance(value, Playlist):
            return Playlist(self.songs + value.songs)
        elif isinstance(value, Song):
            return Playlist(self.songs.append(value))
        else:
            raise TypeError(
                f"Can only add Playlist and Song (not '{type(value)}') to Playlist"
            )

    def __radd__(self, value):
        if isinstance(value, Playlist):
            return Playlist(value.songs + self.songs)
        elif isinstance(value, Song):
            return Playlist(self.songs.insert(0, value))
        else:
            raise TypeError(
                f"Can only add Playlist and Song (not '{type(value)}') to Playlist"
            )

    def __getitem__(self, key):
        return self.songs[key]

    def __setitem__(self, key, value):
        if not isinstance(value, Song):
            raise TypeError(f"Can only set Song (not '{type(value)}')")

        self.songs[key] = value


if __name__ == "__main__":
    song1 = Song(title="Test", album="My album", artist="John")
    song2 = Song(title="Country song", album="Country top 10", artist="Tom")

    playlist = Playlist()

    playlist + song1

    playlist1 = Playlist(songs=[song2])

    playlist2 = playlist + playlist1

    playlist2.__getitem__(1)
    playlist2.__setitem__(0, song1)
