from dotenv import load_dotenv, find_dotenv
from models.engine import FileStorage

# load the var from the .env file into process environments
load_dotenv(find_dotenv())
storage = FileStorage()
storage.reload()

