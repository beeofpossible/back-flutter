from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres.ztyvkhiubnyqmduxbndr:Pommepoire2024#@aws-0-eu-west-3.pooler.supabase.com:6543/postgres"  # Exemple avec SQLite, vous pouvez modifier pour PostgreSQL, MySQL, etc.

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()