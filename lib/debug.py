#!/usr/bin/env python3
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Class import Class
from models.Student import Student
from models.Teacher import Teacher


engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()


@click.command()
@click.option("--name"  , help='Add name')
@click.option("--age", help="Add age")
def hello(name , age):
    click.echo(f"Hello {name} {age} !")

if __name__ == '__main__':
    hello()