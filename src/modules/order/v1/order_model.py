from src.config.db_config import db
from sqlalchemy.orm import relationship
from datetime import datetime
from src.modules.contact.v1.contact_model import ContactModel



class OrderModel(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,primary_key=True)
    contact_id = db.Column(db.Integer,db.ForeignKey("contacts.id"),nullable=False)
    shop_id = db.Column(db.Integer,db.ForeignKey("shops.id"),nullable=False)
