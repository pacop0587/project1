from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.v1.utils.settings import Settings

settings = Settings()

DB_NAME = settings.db_name
DB_USER = settings.db_usr
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




