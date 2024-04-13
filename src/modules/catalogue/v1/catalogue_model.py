from src.config.db_config import db
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import CheckConstraint

"""
    id
    category_id
    title
    price
    inventory

"""

class CatalogueModel(db.Model):
    __tablename__ = "catalogues"
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    shop_id = db.Column(db.Integer,db.ForeignKey("shops.id"))
    title = db.Column(db.String(255),nullable=False)
    price = db.Column(db.Integer,CheckConstraint('price >= 0'))
    inventory = db.Column(db.Integer,CheckConstraint('inventory >= 0'))

    category = relationship('CategoryModel', back_populates="catelogueList",foreign_keys=[category_id])

    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return f"CatalogueModel(id={self.id},category_id={self.category_id},title={self.title},price={self.price},inventory={self.inventory},)"
    
    def to_dict(self):
        return {
            "id":self.id,
            "category_id":self.category_id,
            "shop_id":self.shop_id,
            "title":self.title,
            "price":self.price,
            "inventory":self.inventory,
            "category": self.category.to_dict(),
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }

     # class methods 
    @classmethod
    def add_and_commit(cls,new_catalogue):
        db.session.add(new_catalogue)
        db.session.commit()

