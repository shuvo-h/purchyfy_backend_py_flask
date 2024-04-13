from src.config.db_config import db
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import UniqueConstraint
from src.utils.mixins import BaseMixin



"""
    id
    name
    phone unique
"""


class ContactModel(db.Model,BaseMixin):
    __tablename__= "contacts"
    id = db.Column(db.Integer,primary_key=True)
    name =  db.Column( db.String(100),nullable=False)
    phone =  db.Column( db.String(100),unique=True,nullable=False)

    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    __table_args__ = (
        UniqueConstraint('phone', name='unique_phone'),
    )

    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"ContactModel(id={self.id}, name={self.name}, phone={self.phone},)"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }
    
    # @classmethod
    # def add_and_commit(cls,new_contact):
    #     db.session.add(new_contact)
    #     db.session.commit()