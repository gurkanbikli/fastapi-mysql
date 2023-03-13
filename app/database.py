from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import configuration

engine = create_engine(url=configuration.SQLALCHEMY_DATABASE_URL)

DBSession = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
