#!/usr/bin/env python3
import click
from models.Class import Class
from models.Student import Student
from models.Teacher import Teacher

student=Student()
classes=Class()
teacher=Teacher()

@click.group()
def all_methods():
    pass

# STUDENTS METHODS
@click.command(help='Find all students')
def students():
    click.echo(student.all_students())
all_methods.add_command(students)

@click.command(help='Student full names')
def students_name():
    click.echo(student.full_name())
all_methods.add_command(students_name)

@click.command(help="Add new student")
# @click.option('--name') 
# @click.option(--"first_name",last_name,email,date_of_admission)
# @click.argument('first_name','last_name','email','date')
def new_student():
    student.create_student('shalom','mutuku' ,'2023-9-18')       
all_methods.add_command(new_student)



# TEACHERS METHODS
@click.command(help="All teacher")
def teachers():
    click.echo(teacher.all_teachers())
all_methods.add_command(teachers)

@click.command()
def new_teacher():
    teacher.create_teacher("mark",'munene','programming')  
all_methods.add_command(new_teacher)  


  
if __name__ == '__main__':
    all_methods()