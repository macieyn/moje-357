import datetime
import requests

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.track import Track, Playlist
from app.models.schemas import TrackSchema, PlaylistSchema, PlayEvent

track_schema = TrackSchema()
playlist_schema = PlaylistSchema()


spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


class TrackService:
    @staticmethod
    def get_track_data(track_id):
        """ Get track data by track_id """
        if not (track := Track.query.filter_by(id=track_id).first()):
            return err_resp("Track not found!", "track_404", 404)

        from .utils import load_data

        try:
            track_data = load_data(track)

            resp = message(True, "Track data sent")
            resp["track"] = track_data
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
    
    @staticmethod
    def create_track(data):
        q = data['q']
        response = spotify.search(q, type='track', limit=1)
        result = response["tracks"].get('items')
        if len(result) == 1:
            result = result[0]

        try:
            playlist_name = "Playlista " + datetime.datetime.now().strftime("%d.%m.%Y, %H") + ":00"
            if not (playlist := Playlist.query.filter_by(name=playlist_name).first()):
                playlist = Playlist(
                    name=playlist_name
                )
                db.session.add(playlist)
                db.session.flush()
                db.session.commit()

            if not(track := Track.query.filter_by(spotify_id=result["id"]).first()):
                new_track_name = ", ".join([a.get('name') for a in result["artists"]]) + " - " + result["name"]
                track = Track(
                    name=new_track_name,
                    spotify_id=result["id"]
                )
                db.session.add(track)
                db.session.flush()
                db.session.commit()

            track_playlist_rel = PlayEvent(
                track=track,
                playlist=playlist,
                played_at=datetime.datetime.now()
            )
            db.session.add(track_playlist_rel)
            db.session.flush()
            db.session.commit()

            resp = message(True, "Track has been created.")
            return resp, 201
        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()
