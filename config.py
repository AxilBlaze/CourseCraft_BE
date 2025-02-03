import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    MONGODB_URI = os.getenv('MONGODB_URI')
    HF_API_TOKEN = os.getenv('HF_API_TOKEN')
    MODEL_ID = os.getenv('MODEL_ID')
    VECTOR_STORE_PATH = os.getenv('VECTOR_STORE_PATH')

# ... other config ... 