from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from .service import PlaylistService
from .dto import PlaylistDto

api = PlaylistDto.api
data_resp = PlaylistDto.data_resp


@api.route("/<int:playlist_id>")
class PlaylistGet(Resource):
    @api.doc(
        "Get a specific playlist",
        responses={
            200: ("Playlist data successfully sent", data_resp),
            404: "Playlist not found!",
        },
    )
    # @jwt_required
    def get(self, playlist_id):
        """ Get a specific track's data by track id """
        return PlaylistService.get_playlist_data(playlist_id)



