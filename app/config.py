import os
from dotenv import load_dotenv

load_dotenv('.env.local')

class Settings: 
    GCP_PROJECT_ID: str = os.getenv('GCP_PROJECT_ID')
    FIRESTORE_DATABASE_ID: str = os.getenv('FIRESTORE_DATABASE_ID')
    
settings = Settings()