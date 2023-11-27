# app/models/entity_model.py
def get_entities():
    return {"message": "GET request to /entities"}

def create_entity(data):
    return {"message": "POST request to /entities"}

def update_entity(entity_id, data):
    return {"message": f"PUT request to /entities/{entity_id}"}

def delete_entity(entity_id):
    return {"message": f"DELETE request to /entities/{entity_id}"}
