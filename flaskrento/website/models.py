from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class renting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    renter = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    item_name = db.Column(db.String(200), nullable=False, unique=True)
    item_desc = db.Column(db.String(1000), nullable=False)
    item_price = db.Column(db.String(10000), nullable=False)

    image1 = db.Filefield()
    image1_name = db.Column(db.Text)
    image1_type = db.Column(db.Text)

    image2 = db.Column(db.Text)
    image2_name = db.Column(db.Text)
    image2_type = db.Column(db.Text)

    image3 = db.Column(db.Text)
    image3_name = db.Column(db.Text)
    image3_type = db.Column(db.Text)

    image4 = db.Column(db.Text)
    image4_name = db.Column(db.Text)
    image4_type = db.Column(db.Text)

    security_depo = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    
class rentingadmin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    renter = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    address = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    item_name = db.Column(db.String(200), nullable=False, unique=True)
    item_desc = db.Column(db.String(1000), nullable=False)
    item_price = db.Column(db.String(10000), nullable=False)

    image1 = db.Column(db.Text)
    image1_name = db.Column(db.Text)
    image1_type = db.Column(db.Text)

    image2 = db.Column(db.Text)
    image2_name = db.Column(db.Text)
    image2_type = db.Column(db.Text)

    image3 = db.Column(db.Text)
    image3_name = db.Column(db.Text)
    image3_type = db.Column(db.Text)

    image4 = db.Column(db.Text)
    image4_name = db.Column(db.Text)
    image4_type = db.Column(db.Text)

    security_depo = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    

