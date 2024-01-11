from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import click

Base = declarative_base() 

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='items')
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    supplier = relationship('Supplier', back_populates='supplied_items') 


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    items = relationship('Item', back_populates='category')


class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    supplied_items = relationship('Item', back_populates='supplier')

def create_database():
    Base.metadata.create_all(engine)


def add_category(name):
    new_category = Category(name=name)
    session.add(new_category)
    session.commit() 


def view_items_by_category(category_name):
    category = session.query(Category).filter_by(name=category_name).first()
    if category:
        items = category.items
        if items:
            click.echo(f"\nItems in Category '{category_name}':")
            for item in items:
                click.echo(item.name)
        else:
            click.echo(f"No items found in Category '{category_name}'.")
    else:
        click.echo(f"Category '{category_name}' not found.")