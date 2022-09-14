#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class City(BaseModel, Base if (getenv('HBNB_TYPE_STORAGE') == 'db') else
           object):

    """ The city class, contains state ID and name """

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'cities'
        __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
                          'mysql_collate': 'utf8_general_ci'}
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place",
            backref='cities',
            cascade="all, delete",
            passive_deletes=True)
    else:
        state_id = ""
        name = ""
