import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MONGO_URL = os.getenv("MONGO_URL", "").strip()  # Added for MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()  # Optional, for stats or other DB

# -------------------- Validation -------------------- #
if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
elif not MONGO_URL:
    raise SystemExit("No MONGO_URL found. Exiting...")  # Ensure Mongo is present

# -------------------- Type Correction -------------------- #
try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

# Fix DATABASE_URL if using PostgreSQL
if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
