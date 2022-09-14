#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv


class Review(BaseModel, Base if (getenv('HBNB_TYPE_STORAGE') == 'db') else
             object):
    """ Review classto store review information """
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'reviews'
        __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
                          'mysql_collate': 'utf8_general_ci'}
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
