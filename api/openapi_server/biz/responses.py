from flask import jsonify

def invalid_uuid(id):
    return bad_request(f"Invalid UUID: {id}")

def bad_request(message: str = ""):
    return jsonify({"error": message}), 400

def task_not_found(task_id):
    return item_not_found("Task", task_id)

def category_not_found(category_id):
    return item_not_found("Category", category_id)

def item_not_found(name: str, id: str):
    return not_found(f"{name} not found: {id}")

def not_found(message):
    return jsonify({"error": message}), 404