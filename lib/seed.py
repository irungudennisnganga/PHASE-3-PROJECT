from faker import Faker
from datetime import date
from models.Class import Class
from models.Student import Student
from models.Teacher import Teacher
from models.base import session
import random

fake = Faker()

session.query(Class).delete()
session.query(Student).delete()
session.query(Teacher).delete()

# Create some teachers
teachers = [
    Teacher(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        subject=fake.word(),
        email=fake.email()
    ) for _ in range(0)
]


# Create some classes, assigning teachers randomly
# classes = [
#     Class(
#         name=f"Class {i + 1}",
#         # level=random.choice(["Beginner", "Intermediate", "Advanced"]),
#         teacher=random.choice(teachers),
#         student=random.choice(Student)
#     ) for i in range(4)
# ]


# Create some students and assign them to classes randomly
students = [
    Student(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        date_of_admission=fake.date_between(start_date="-1y", end_date="today"),
        # classes=[random.choice(classes)]
    ) for _ in range(0)
]

# Create some classes, assigning teachers randomly
classes = [
    Class(
        name=f"Class {i + 1}",
        # level=random.choice(["Beginner", "Intermediate", "Advanced"]),
        teacher=random.choice(teachers),
        student=random.choice(students)
    ) for i in range(0)
]


# Add all objects to the session and commit
session.add_all(teachers)
session.add_all(classes)
session.add_all(students)
session.commit()
