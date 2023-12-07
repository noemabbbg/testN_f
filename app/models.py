from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Comic(Base):
    __tablename__ = "comics"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    rating = Column(Float, default=0)

class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True, index=True)
    comic_id = Column(Integer, ForeignKey('comics.id'))
    user_id = Column(Integer, index=True)
    value = Column(Integer, index=True)

    comic = relationship("Comic", back_populates="ratings")

Comic.ratings = relationship("Rating", order_by=Rating.id, back_populates="comic")
