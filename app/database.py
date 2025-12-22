from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import create_engine
from app.config import *

Base = declarative_base()
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(bind = engine, autoflush=False, autocommit = False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
