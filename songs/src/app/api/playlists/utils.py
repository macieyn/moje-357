def load_data(playlist_db_obj):
    """ Load playlist's data

    Parameters:
    - Playlist db object
    """
    from app.models.schemas import PlaylistSchema

    playlist_schema = PlaylistSchema()

    data = playlist_schema.dump(playlist_db_obj)

    return data
