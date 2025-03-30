from app.models.user import users_collection
from app.schemas.user_schema import UserSchema
from bson import ObjectId

# Create a new user
def create_user(user: UserSchema):
    user_dict = user.dict()
    user_dict["_id"] = str(ObjectId())  # Convert MongoDB _id to string
    users_collection.insert_one(user_dict)
    return {"message": "User created successfully", "user_id": user_dict["_id"]}

# Get all users
def get_users():
    users = users_collection.find({}, {"_id": 1, "name": 1, "email": 1})  # Only return name & email
    return [{"id": str(user["_id"]), "name": user["name"], "email": user["email"]} for user in users]
