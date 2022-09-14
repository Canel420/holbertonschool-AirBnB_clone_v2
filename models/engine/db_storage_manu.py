#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session


user = getenv('HBNB_MYSQL_USER')
password = getenv('HBNB_MYSQL_PWD')
host = getenv('HBNB_MYSQL_HOST')
database = getenv('HBNB_MYSQL_DB')
env = getenv('HBNB_ENV')


class DBStorage():
    """ This class manages storage of hbnb models in MySQl database """
    __classes = [User, State, City, Amenity, Place, Review]
    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of class DBStorage """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,  password, host, database),
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method to return existing classes in database """
        result = {}
        if cls in self.__classes:
            search = self.__session.query(cls)
            for obj in search:
                key = f'{obj.__class__.__name__}.{obj.id}'
                result[key] = obj
        elif cls is None:
            for clas in self.__classes:
                search = self.__session.query(clas)
                for obj in search:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    result[key] = obj
        return(result)

    def new(self, obj):
        """ Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session object """
        self.__session.delete(obj)

    def reload(self):
        """ Reload de database saved objects to MySQL """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ close the class Session """
        self.__session.close()
