#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import Float, Integer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.review import Review
import models
from os import getenv


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False)
)


class Place(BaseModel, Base if (getenv('HBNB_TYPE_STORAGE') == 'db') else
            object):
    """ A place to stay """
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship(
            'Review',
            backref='state',
            cascade="all, delete, delete-orphan"
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ Getter that that returns the list of Reviews instances """
            instances = models.storage.all('Review')
            new = []
            for review in instances.values():
                if review.place_id == (self.id):
                    new.append(review)
            return new

        @property
        def amenities(self):
            """
            Getter attribute amenities that returns the list of Amenity
            instances
            """
            new = []
            instances = models.storage.all('Amenity').values()
            for amenity in instances:
                if amenity.amenity_ids == self.id:
                    new.append(amenity)
            return new

        @reviews.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids.
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
