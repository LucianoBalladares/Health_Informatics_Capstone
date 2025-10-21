import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from the .env file in project root
load_dotenv()

def get_engine():
    """
    Create and return a SQLAlchemy engine using credentials stored in .env.
    This avoids hardcoding sensitive information into scripts or notebooks.
    """
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")

    if not all([db_user, db_pass, db_name]):
        raise ValueError("Missing one or more database credentials in .env file.")

    connection_string = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(connection_string)
    return engine