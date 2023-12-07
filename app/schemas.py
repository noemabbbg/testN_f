from pydantic import BaseModel

class ComicBase(BaseModel):
    title: str
    author: str

class ComicCreate(ComicBase):
    pass

class Comic(ComicBase):
    id: int
    rating: float

    class Config:
        orm_mode = True

class RatingBase(BaseModel):
    comic_id: int
    user_id: int
    value: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True
