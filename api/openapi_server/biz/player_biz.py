from openapi_server.models.update_player_request import UpdatePlayerRequest  # noqa: E501
from openapi_server.models.player import Player  # noqa: E501
from ..models.category import Category

from .. import db

from ..database import models

from .responses import *
from .mappers import *
from .helpers import *

def get_player(discord_id) -> Player:
    player = models.Player.query.filter_by(discord_id=discord_id).first()
    if not player:
        player = models.Player(
            discord_id = discord_id,
            score = 0
        )
        db.session.add(player)
        db.session.commit()
    
    return map_db_player_to_player(player)

def update_player(player_id, update_player_request: UpdatePlayerRequest) -> Player:
    if not (validate_uuid(player_id)):
        return invalid_uuid(player_id)

    to_update = models.Player.query.get(player_id)
    if not to_update:
        return player_not_found(player_id)
    
    to_update.points = update_player_request.points

    db.session.commit()

    return map_db_player_to_player(to_update)

def add_category_to_player(player_id, category_id) -> Player:
    if not (validate_uuid(player_id)):
        return invalid_uuid(player_id)

    player = models.Player.query.get(player_id)
    if not player:
        return player_not_found(player_id)
    
    if not (validate_uuid(category_id)):
        return invalid_uuid(category_id)

    category = models.Category.query.get(category_id)
    if not category:
        return category_not_found(category_id)
    
    if not category in player.categories:
        player.categories.append(category)
        db.session.commit()
    
    return map_db_player_to_player(player)

def remove_category_from_player(player_id, category_id) -> Player:
    if not (validate_uuid(player_id)):
        return invalid_uuid(player_id)

    player = models.Player.query.get(player_id)
    if not player:
        return player_not_found(player_id)
    
    if not (validate_uuid(category_id)):
        return invalid_uuid(category_id)

    category = models.Category.query.get(category_id)
    if not category:
        return category_not_found(category_id)
    
    if category in player.categories:
        player.categories.remove(category)
        db.session.commit()
    
    return map_db_player_to_player(player)