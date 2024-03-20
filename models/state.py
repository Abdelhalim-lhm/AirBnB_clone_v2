#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            city_list = []
            cities_dict = storage.all(City)
            for city_id, city in cities_dict.items():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
