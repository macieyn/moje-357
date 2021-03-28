from flask_restx import Api
from flask import Blueprint

from .tracks.controller import api as track_ns
from .playlists.controller import api as playlist_ns

# Import controller APIs as namespaces.
api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="Main routes.")

# API namespaces
api.add_namespace(track_ns)
api.add_namespace(playlist_ns)
