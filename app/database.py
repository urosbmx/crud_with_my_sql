import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# Construct the database connection URL using environment variables
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', 3306)}/{os.getenv('DB_NAME')}"

# Create the SQLAlchemy engine to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for declarative models
Base = declarative_base()
