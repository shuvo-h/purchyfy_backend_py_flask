from src.config.db_config import db
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.orm import relationship
from datetime import datetime

class UserRole:
    ADMIN = 'admin'
    USER = 'user'


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique=True,nullable=False)
    role = db.Column(db.Enum(UserRole.USER, UserRole.ADMIN,name='user_role_enum'), nullable=False, default=UserRole.USER,)
    name= db.Column(db.String(100),nullable=True)
    password = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    # relationship 
    shopList = relationship("ShopModel",back_populates="owner")   # one to many relation

    def __init__(self,email,password,name,role):
        self.email = email
        self.password = password
        self.role = role
        self.name = name
    
    def set_password(self,plain_password):
        self.password = generate_password_hash(plain_password)
    
    def check_password(hashed_password,plain_password):
        return check_password_hash(hashed_password,plain_password)
    
    # printer methods
    def __str__(self):
        return f"User(id={self.id}, email={self.email}), role={self.role}"

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'role': self.role.value,
            'name': self.name,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt,
        }
    
    # class methods 
    @classmethod
    def add_and_commit(cls,new_user):
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def is_email_valid(email):
        # Implement your email validation logic here
        # Return True if the email is valid, otherwise False
        pass


