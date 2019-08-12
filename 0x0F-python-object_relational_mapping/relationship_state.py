#!/usr/bin/python3

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""
    class definition of a State and an instance Base = declarative_base()
"""


class State(Base):

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref='state')
