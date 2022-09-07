#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.place import Place
from sqlalchemy import Column, String



class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
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
