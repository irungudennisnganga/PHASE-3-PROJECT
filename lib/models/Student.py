#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String,ForeignKey,Date
from sqlalchemy.orm import relationship
from .base import Base,session

class Student(Base):
    __tablename__ = "students"

    id= Column(Integer , primary_key=True)
    name=Column(String)
    email =Column(String)
    date_of_admission=Column(Date)
    
    # class_id=Column(Integer ,ForeignKey("classes.id") )
    
    classes=relationship("Class", back_populates="student")

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Email {self.email}" \
            + f"Date of admission {self.date_of_admission}"    