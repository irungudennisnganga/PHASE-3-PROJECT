#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String,ForeignKey,Date
from sqlalchemy.orm import relationship
from .base import Base,session

class Student(Base):
    __tablename__ = "students"

    id= Column(Integer , primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email =Column(String)
    date_of_admission=Column(Date)
    

    
    classes=relationship("Class", back_populates="student")
    # classes = relationship("Class", lazy="dynamic")
    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.first_name}, " \
            + f"{self.last_name}" \
            + f"Email {self.email}" \
            + f"Date of admission {self.date_of_admission}"       