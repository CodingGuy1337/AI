import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Now these are accessible across all your scripts
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
DATA_FOLDER = os.getenv("DATA_FOLDER", "training_data/")
