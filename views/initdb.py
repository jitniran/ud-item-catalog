from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base

engine = create_engine('sqlite:///sportitems.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
