import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    MONGODB_URI = os.getenv('MONGODB_URI')
    HF_API_TOKEN = os.getenv('HF_API_TOKEN')
    
    # Different model IDs for different purposes
    FLAN_T5_MODEL = os.getenv('FLAN_T5_MODEL')  # For general text generation
    OPT_MODEL = os.getenv('OPT_MODEL')          # For optimization tasks
    GPT2_MODEL = os.getenv('GPT2_MODEL')        # For text completion
    DIALOGPT_MODEL = os.getenv('DIALOGPT_MODEL') # For conversational tasks
    
    VECTOR_STORE_PATH = os.getenv('VECTOR_STORE_PATH')

# ... other config ... 