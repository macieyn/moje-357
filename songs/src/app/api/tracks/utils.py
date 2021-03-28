def load_data(track_db_obj):
    """ Load track's data

    Parameters:
    - Track db object
    """
    from app.models.schemas import TrackSchema

    track_schema = TrackSchema()

    data = track_schema.dump(track_db_obj)

    return data
