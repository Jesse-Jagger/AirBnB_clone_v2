#!/usr/bin/python3
"""the state module for amenity"""

import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """the Amenity class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        place_amenities = relationship("Place", secondary="place_amenity")
