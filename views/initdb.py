from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base, Sport, SportItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()