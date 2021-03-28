from flask_restx import Namespace, fields


class TrackDto:

    api = Namespace("track", description="Track related operations.")
    track_obj = api.model(
        "Track object",
        {
            "id": fields.Integer,
            "name": fields.String,
            "spotify_id": fields.String,
            "played_at": fields.DateTime,
        },
    )

    data_resp = api.model(
        "Track Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "track": fields.Nested(track_obj),
        },
    )

