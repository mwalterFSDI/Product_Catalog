from app import db 
from app.database import product

def create_my_user(name, price, quantity):
    
    db.session.add(
        Product(
            name=name,
            price=price,
            quantity=quantity
        )
    )
db.session.commit()

if__name__="__main__":
    create_my_product("Apples", "10.00", "10")
    products = Product.query.all()
    print(products)
    create_my_user("oranges", "12.00", "20")
    