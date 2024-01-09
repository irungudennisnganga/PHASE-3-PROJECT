#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base,session

class Teacher(Base):
    __tablename__ = "teachers"

    id= Column(Integer , primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    subject=Column(String)
    email =Column(String)
    
    
    classes=relationship("Class" ,back_populates="teacher")
    
    def __repr__(self):
        return f"Teacher {self.id}: " \
            + f"{self.first_name}, " \
            + f"{self.last_name}" \
            +  f"Subject {self.subject}" \
            +  f"Email {self.email}" 