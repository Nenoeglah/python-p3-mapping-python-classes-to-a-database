
from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song


@classmethod
def get_all_songs(cls):
    CURSOR.execute("SELECT * FROM songs")
    songs = CURSOR.fetchall()
    return [cls(*song[1:]) for song in songs]

if __name__ == "__main__":
    Song.create_table()
