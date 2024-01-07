#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base,session

class Class(Base):
    __tablename__='classes'

    id=Column(Integer, primary_key=True)
    name=Column(String)
