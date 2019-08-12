#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
    class definition of a City
"""


class City(Base):

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'), nullable=False)
