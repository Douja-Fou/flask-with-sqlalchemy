# wsgi.py
import os
import logging


from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema
from schemas import product_schema

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)

@app.route('/products/id', methods=['GET'])
def read_product():
    product = db.session.query(Product).get(1) # SQLAlchemy request => 'SELECT * FROM products'
    print(product)
    return product_schema.jsonify(product)

@app.route('/addproducts', methods=['POST'])
def add_product():
    newproduct = Product(name = "newProducts")
    db.session.add(newproduct) # SQLAlchemy request => 'SELECT * FROM products'
    db.session.commit()
    products = db.session.query(Product).all()
    return products_schema.jsonify(products)

@app.route('/delproducts', methods=['DELETE'])
def del_product():
    delproduct = db.session.query(Product).get(1)
    db.session.delete(delproduct) # SQLAlchemy request => 'SELECT * FROM products'
    db.session.commit()
    products = db.session.query(Product).all()
    return products_schema.jsonify(products)

@app.route('/updateproducts/<int:prd_id>', methods=['PATCH'])
def update_product(prd_id):
    updateprd=db.session.query(Product).filter(Product.id == prd_id).update({'name' : 'newnae'})
    db.session.commit()
    products = db.session.query(Product).all()
    return products_schema.jsonify(products)
