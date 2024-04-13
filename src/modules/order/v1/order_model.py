from src.config.db_config import db
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Enum
from src.utils.mixins import BaseMixin

"""
    id
    shop_id
    contact_id
    total_price
    order_items: [{}]

"""

# Define the enum values separately
ORDER_STATUS = {
    "PENDING": "pending",
    "RUNNING": "running",
    "CANCELLED": "cancelled",
    "COMPLETED": "completed"
}

class OrderModel(db.Model,BaseMixin):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    contact_id = db.Column(db.Integer,db.ForeignKey("contacts.id"),nullable=False)
    shop_id = db.Column(db.Integer,db.ForeignKey("shops.id"),nullable=False)
    total_price = db.Column(db.Float,nullable=False)
    order_items = db.Column(db.JSON,nullable=False) 
    status = db.Column(db.Enum(*ORDER_STATUS.values(), name="order_status_enum"), nullable=False)

    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def __init__(self, contact_id, shop_id, total_price, order_items,status):
        self.contact_id = contact_id
        self.shop_id = shop_id
        self.total_price = total_price
        self.order_items = order_items
        self.status = status

    

    def to_dict(self):
        # Populate the dictionary with the attributes
        order_dict = {
            'id': self.id,
            'contact_id': self.contact_id,
            'shop_id': self.shop_id,
            'total_price': self.total_price,
            'order_items': self.order_items,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }

        # If the related objects are available, include their attributes in the dictionary
        # if self.contact:
        #     order_dict['contact'] = self.contact.to_dict()
        
        # if self.shop:
        #     order_dict['shop'] = self.shop.to_dict()

        return order_dict

    
     # class methods 
    # @classmethod
    # def add_and_commit(cls,new_order):
    #     db.session.add(new_order)
    #     db.session.commit()
