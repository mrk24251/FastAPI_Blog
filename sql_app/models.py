from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import datetime
from sqlalchemy_utils import EmailType

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(EmailType, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    # post = relationship("Post", back_populates="owner")

#
# class Post(Base):
#     __tablename__ = "post"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     body = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     owner = relationship("User", back_populates="post")
#     comment = relationship("Comment", back_populates="related_post")
#
# class Comment(Base):
#     __tablename__ = "comment"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(EmailType)
#     body = Column(String)
#     is_active = Column(Boolean, default=False)
#     created_date = Column(DateTime, default=datetime.datetime.utcnow)
#
#     related_post = relationship("Post", back_populates="comment")