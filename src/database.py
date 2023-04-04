import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
Base = declarative_base()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
