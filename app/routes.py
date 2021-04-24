#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Routes definitions"""


from app import app
from datetime import datetime

@app.route("/version")
def version():
    return{
        "ok": True, 
        "message": "success",
        "version": "1.0.0",
        "server time": datetime.now().strftiime("%F%H:%M:%S")
    }

@app.route("/products")
def get_products():
    """Retrieve all products"""
    pass

@app.route("/products/<int:pid>")
def get_product_detail(pid):
    """retrieve a single product"""
    pass
@app.route("/products/<int:pid>", methods=["PUT"])
    """Create a new product"""
    pass

@app.route("/products/<int:pid>", methods=["DELETE"])
    """Soft delete a single product""
    return "Soft delete a product"