# Model Schemas
from marshmallow_sqlalchemy.fields import Nested

from app import ma

from .track import Track, Playlist, PlayEvent


class TrackSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Track

    name = ma.auto_field()
    spotify_id = ma.auto_field()


class PlaylistSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Playlist
        include_relationships = True
    
    name = ma.auto_field()
    play_events = Nested('PlayEventSchema', many=True)


class PlayEventSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PlayEvent
        include_relationships = True
    
    played_at = ma.auto_field()
    track = ma.Nested(TrackSchema)

    
