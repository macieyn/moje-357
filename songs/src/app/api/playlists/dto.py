from flask_restx import Namespace, fields

from app.api.tracks.dto import TrackDto


class PlaylistDto:

    api = Namespace("playlist", description="Playlist related operations.")
    playlist_obj = api.model(
        "Playlist object",
        {
            "id": fields.Integer,
            "name": fields.String,
            "tracks": fields.List(fields.Nested(TrackDto.track_obj))
        },
    )

    data_resp = api.model(
        "Playlist Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "track": fields.Nested(playlist_obj),
        },
    )

