from datetime import datetime
from app import db, bcrypt

# Alias common DB names
Column = db.Column
Model = db.Model


class PlayEvent(Model):
    __tablename__ = 'playevents'
    id = Column(db.Integer, primary_key=True)
    track_id = Column(db.Integer, db.ForeignKey('tracks.id'))
    playlist_id = Column(db.Integer, db.ForeignKey('playlists.id'))
    played_at = Column(db.DateTime)
    track = db.relationship("Track")
    playlist = db.relationship("Playlist")

    def __repr__(self):
        return f"<PlayEvent - {self.id}>"


class Track(Model):
    __tablename__ = "tracks"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(200))
    spotify_id = Column(db.String(30))

    play_events = db.relationship("PlayEvent", back_populates="track")

    def __repr__(self):
        return f"<Track - {self.id}>"


class Playlist(Model):
    __tablename__ = "playlists"
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(200))

    play_events = db.relationship("PlayEvent", back_populates="playlist")

    def __repr__(self):
        return f"<Playlist - {self.id}>"

