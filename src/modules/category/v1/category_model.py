from src.config.db_config import db
from sqlalchemy.orm import relationship
from datetime import datetime

"""
    id
    shop_id
    title
"""

class CategoryModel(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)
    shop = relationship("ShopModel",back_populates="categoryList",foreign_keys=[shop_id])
    catelogueList = relationship("CatalogueModel", back_populates="category",)

    title = db.Column(db.String(255),nullable=False)

    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def __init__(self,shop_id,title) :
        self.shop_id = shop_id
        self.title = title

    def __str__(self):
        return f"CategoryModel(id={self.id}, shop_id={self.shop_id}, title={self.title})"

    def to_dict(self):
        # shop_info = self.shop.to_dict()  # Fetch shop info
        category_dict = {
            "id": self.id,
            "shop_id": self.shop_id,
            "title": self.title,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }
        
        return category_dict

    
     # class methods 
    @classmethod
    def add_and_commit(cls,new_category):
        db.session.add(new_category)
        db.session.commit()