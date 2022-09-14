#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv


class User(BaseModel, Base if (getenv('HBNB_TYPE_STORAGE') == 'db') else
           object):
    """This class defines a user by various attributes"""
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'users'
        __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
                          'mysql_collate': 'utf8_general_ci'}
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship(
            "Place",
            backref='user',
            cascade="all, delete",
            passive_deletes=True)
        reviews = relationship(
            "Review",
            backref='user',
            cascade="all, delete",
            passive_deletes=True)
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
