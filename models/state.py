#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City',
        cascade='all, delete, delete-orphan',
        backref='state'
    )

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns the cities in this State"""
            cities_in_state = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
