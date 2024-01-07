#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base,session

class Teacher(Base):
    __tablename__ = "teachers"

    id= Column(Integer , primary_key=True)
    name=Column(String)
    email =Column(String)
    
    def __repr__(self):
        return f"Teacher {self.id}: " \
            + f"{self.name}, " \
            + f"Email {self.email}"