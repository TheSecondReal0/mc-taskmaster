import uuid

def validate_uuid(_uuid) -> bool:
    try:
        uuid.UUID(_uuid, version=4)
    except ValueError:
        return False
    return True