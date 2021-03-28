from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import TrackService
from .dto import TrackDto

api = TrackDto.api
data_resp = TrackDto.data_resp


@api.route("/")
class TrackPost(Resource):
    @api.doc(
        "Create a specific track",
        responses={
            201: ("Track data successfully created", data_resp),
            400: "Bad request!",
        },
    )
    # @jwt_required
    def post(self):
        """ Create a track based on posted data """
        data = request.get_json()
        return TrackService.create_track(data)


@api.route("/<int:track_id>")
class TrackGet(Resource):
    @api.doc(
        "Get a specific track",
        responses={
            200: ("Track data successfully sent", data_resp),
            404: "Track not found!",
        },
    )
    # @jwt_required
    def get(self, track_id):
        """ Get a specific track's data by track id """
        return TrackService.get_track_data(track_id)



