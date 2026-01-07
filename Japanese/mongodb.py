import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# -------------------- Mongo Config -------------------- #

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise RuntimeError("❌ MONGO_URL environment variable not found!")

# -------------------- Mongo Client -------------------- #

try:
    mongo_client = MongoClient(
        MONGO_URL,
        serverSelectionTimeoutMS=5000
    )
    mongo_client.server_info()  # Test connection
except ServerSelectionTimeoutError:
    raise RuntimeError("❌ Failed to connect to MongoDB")

# -------------------- Database & Collections -------------------- #

db = mongo_client["TeamJapanese"]

users_col = db["users"]
groups_col = db["groups"]

# -------------------- Save User -------------------- #

async def save_user(user):
    """
    Save / Update private users
    """
    if not user:
        return

    data = {
        "_id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "is_bot": user.is_bot,
    }

    users_col.update_one(
        {"_id": user.id},
        {"$set": data},
        upsert=True
    )

# -------------------- Save Group -------------------- #

async def save_group(chat):
    """
    Save / Update groups & supergroups
    """
    if not chat or chat.type not in ["group", "supergroup"]:
        return

    data = {
        "_id": chat.id,
        "title": chat.title,
        "username": chat.username,
        "type": chat.type,
    }

    groups_col.update_one(
        {"_id": chat.id},
        {"$set": data},
        upsert=True
    )

# -------------------- Stats -------------------- #

def total_users():
    return users_col.count_documents({})

def total_groups():
    return groups_col.count_documents({})

# -------------------- Broadcast Helpers -------------------- #

def get_all_users():
    return users_col.find({}, {"_id": 1})

def get_all_groups():
    return groups_col.find({}, {"_id": 1})


# -------------------- Counts -------------------- #

def get_users_count():
    return users_col.count_documents({})

def get_groups_count():
    return groups_col.count_documents({})


# -------------------- IDs Fetch -------------------- #

def get_all_user_ids():
    return [u["_id"] for u in users_col.find({}, {"_id": 1})]

def get_all_group_ids():
    return [g["_id"] for g in groups_col.find({}, {"_id": 1})]


# -------------------- Auto Remove -------------------- #
# -------------------- Remove user/group -------------------- #
def remove_user(user_id: int):
    """
    Remove a user from DB if failed
    """
    users_col.delete_one({"_id": user_id})

def remove_group(group_id: int):
    """
    Remove a group from DB if failed
    """
    groups_col.delete_one({"_id": group_id})
