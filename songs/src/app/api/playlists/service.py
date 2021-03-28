import datetime
import requests

from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.track import Playlist
from app.models.schemas import PlaylistSchema

playlist_schema = PlaylistSchema()
playlists_schema = PlaylistSchema(many=True)


class PlaylistService:
    @staticmethod
    def get_playlist_data(playlist_id):
        """ Get playlist data by playlist_id """
        if not (playlist := Playlist.query.filter_by(id=playlist_id).first()):
            return err_resp("Playlist not found!", "playlist_404", 404)

        from .utils import load_data

        try:
            playlist_data = load_data(playlist)

            resp = message(True, "Playlist data sent")
            resp["playlist"] = playlist_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
    
    @staticmethod
    def get_all_data():
        """ Get all playlists data """
        playlists = Playlist.query.all()

        try:
            playlist_data = playlists_schema.dump(playlists)

            resp = message(True, "Playlists data sent")
            resp["playlists"] = playlist_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
    
    