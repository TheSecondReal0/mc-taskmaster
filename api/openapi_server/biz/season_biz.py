from ..models.category import Category

from .. import db

from ..database import models

def get_current_season() -> models.Season:
    return models.Season.query.first()