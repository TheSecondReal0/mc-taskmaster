from openapi_server.models.get_categories200_response import GetCategories200Response  # noqa: E501
from openapi_server.models.create_category_request import CreateCategoryRequest  # noqa: E501
from ..models.category import Category

from .. import db

from ..database import models

from .responses import *
from .mappers import *
from .helpers import *

def get_categories() -> GetCategories200Response:
    categories = models.Category.query.all()

    mapped = map_db_categories_to_categories(categories)
    
    return GetCategories200Response(
        mapped,
        len(mapped)
    )

def get_category(category_id) -> Category:
    if not (validate_uuid(category_id)):
        return invalid_uuid(category_id)

    category = models.Category.query.get(category_id)
    if not category:
        return category_not_found(category_id)
    
    return map_db_category_to_category(category)

def create_category(create_category_request: CreateCategoryRequest) -> Category:
    to_insert: models.Category = models.Category(
        name = create_category_request.name
        )

    db.session.add(to_insert)
    db.session.commit()

    return map_db_category_to_category(to_insert)

def update_category(category_id, create_category_request: CreateCategoryRequest) -> Category:
    if not (validate_uuid(category_id)):
        return invalid_uuid(category_id)

    to_update = models.Category.query.get(category_id)
    if not to_update:
        return category_not_found(category_id)
    
    to_update.name = create_category_request.name

    db.session.commit()

    return map_db_category_to_category(to_update)

def delete_category(category_id):
    if not (validate_uuid(category_id)):
        return invalid_uuid(category_id)

    category = models.Category.query.get(category_id)
    if not category:
        return category_not_found(category_id)
    
    db.session.delete(category)
    db.session.commit()
