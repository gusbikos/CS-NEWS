import os
from dotenv import load_dotenv

# Load environment variables from backend/.env
load_dotenv()

# Get FACEIT API key
FACEIT_API_KEY = os.getenv("FACEIT_API_KEY")