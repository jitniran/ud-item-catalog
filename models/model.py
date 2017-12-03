import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Sport(Base):
    __tablename__ = 'sport'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """
        return json sport
        """
        return{
            'id':self.id,
            'name':self.name,
        }


class SportItem(Base):
    __tablename__ = 'sport_item'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    sport_id = Column(Integer,ForeignKey('sport.id'))
    sport = relationship(Sport) 

    @property
    def serialize(self):
        """
        return json SportItem
        """
        return{
            'id':self.id,
            'sport_id':self.sport_id,
            'title':self.name,
            'description':self.description,
            'price':self.price,
        }


engine = create_engine('sqlite:///sportitems.db')
Base.metadata.create_all(engine)