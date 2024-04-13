from src.config.db_config import db
from sqlalchemy.orm import relationship
from datetime import datetime



"""
    id
    user_id
    shop_name
    address:{
        road
        city
        state
        country
        post
        location:{
            lat,
            lang
        }
    }
    owner
"""


class ShopModel(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column( db.Integer,  db.ForeignKey('users.id'), nullable=False)

    shop_name =  db.Column( db.String(100),nullable=False)
    address =  db.Column(db.JSON,nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    # relationship (one to many)
    owner = relationship('UserModel',back_populates='shopList') # one to many relation
    categoryList = relationship("CategoryModel", back_populates="shop")

    def __init__(self,user_id,shop_name,address):
        self.user_id = user_id
        self.shop_name = shop_name
        self.address = address

    def __str__(self):
        return f"ShopModel(id={self.id}, shop_name={self.shop_name},)"
    def to_dict(self):
        owner = {
            "id": self.owner.id,
            "email": self.owner.email,
            "name": self.owner.name,
            # "role": self.owner.role
        } if self.owner else None

        categories = [category.to_dict() for category in self.categoryList]
         
        return {
            "id": self.id,
            "user_id": self.user_id,
            "shop_name": self.shop_name,
            "address": {
                "road": self.address.get('road'),
                "city": self.address.get('city'),
                "state": self.address.get('state'),
                "country": self.address.get('country'),
                "post": self.address.get('post'),
                "location": {
                    "lat": self.address.get('location', {}).get('lat'),
                    "lang": self.address.get('location', {}).get('lang')
                }
            },
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
            "owner": owner,
            "categoryList": categories
        }

     # class methods 
    @classmethod
    def add_and_commit(cls,new_shop):
        db.session.add(new_shop)
        db.session.commit()


    @staticmethod
    def is_lat_lang_valid(lat,lang):
        # Implement the lat lang validation logic here
        # Return True if it is valid, otherwise False
        pass
