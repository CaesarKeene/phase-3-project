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

def add_item(name, category_name, supplier_name):
    category = session.query(Category).filter_by(name=category_name).first()
    supplier = session.query(Supplier).filter_by(name=supplier_name).first()
    
    if category and supplier:
        new_item = Item(name=name, category=category, supplier=supplier)
        session.add(new_item)
        session.commit()
        click.echo(f"Item '{name}' added to Category '{category_name}' from Supplier '{supplier_name}' successfully.")
    else:
        if not category:
            click.echo(f"Category '{category_name}' not found. Please add the category first.")
        if not supplier:
            click.echo(f"Supplier '{supplier_name}' not found. Please add the supplier first.") 

def remove_item(name):
    item = session.query(Item).filter_by(name=name).first()
    if item:
        session.delete(item)
        session.commit()
        click.echo(f"Item '{name}' removed from inventory.")
    else:
        click.echo(f"Item '{name}' not found in inventory.") 

def add_supplier(name):
    new_supplier = Supplier(name=name)
    session.add(new_supplier)
    session.commit()
    click.echo(f"Supplier '{name}' added successfully.")

def view_suppliers():
    suppliers = session.query(Supplier).all()
    if suppliers:
        click.echo("\nSuppliers:")
        for supplier in suppliers:
            click.echo(supplier.name)
    else:
        click.echo("No suppliers in the database.")


@click.command()
def main():
    create_database()

    while True:
        click.echo("\nInventory Management System")
        click.echo("1. Add Category")
        click.echo("2. View Items by Category")
        click.echo("3. Add Item")
        click.echo("4. Remove Item")
        click.echo("5. Add Supplier")
        click.echo("6. View Suppliers")
        click.echo("7. Exit")
        choice = click.prompt("Enter your choice (1-7)", type=int) 