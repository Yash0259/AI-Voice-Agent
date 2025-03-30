from app.models.user import users_collection
from app.schemas.user_schema import UserSchema
from bson import ObjectId

def create_user(user : UserSchema):
    user_dist : user.dict()
    user_dict["id"] = str(ObjectId()) // convert mongoDB _id to string
    users_collection.insert_one(user_dict)
    return{ "message":"User created Successfully","user_id":user_dict["_id"]}

def get_users():
    users = users_collection.find({},{"_id":1,"name":1,"email":1})
    return[{"id":str(user["_id"]),"name":user["name"],"email":user["email"]} for user in users]