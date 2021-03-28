import datetime
import requests

from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.track import Playlist


class PlaylistService:
    @staticmethod
    def get_playlist_data(playlist_id):
        """ Get track data by playlist_id """
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
    
    