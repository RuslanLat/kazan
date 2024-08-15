from dataclasses import dataclass
from typing import Optional
from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
)

from app.store.database.sqlalchemy_base import db


@dataclass
class Card:
    card_id: Optional[int]
    title: str
    image: str
    price_min: int
    price_max: int
    genre_title: str
    genre_name: str
    location: str
    address: str
    is_pushkins_card: bool
    details: str
    description: str


class CardModel(db):

    __tablename__ = "cards"

    card_id = Column(Integer, primary_key=True)
    title = Column(String)
    image = Column(String)
    price_min = Column(Integer)
    price_max = Column(Integer)
    genre_title = Column(String)
    genre_name = Column(String)
    location = Column(String)
    address = Column(String)
    is_pushkins_card = Column(Boolean, default=True)
    details = Column(String)
    description = Column(String)
