from typing import List, Optional
from sqlalchemy import select, update, delete, and_
from sqlalchemy.orm import joinedload
from app.cards.models import Card, CardModel
from app.base.base_accessor import BaseAccessor


class CardAccessor(BaseAccessor):

    async def list_cards(self) -> List[Optional[Card]]:
        query = select(CardModel).limit(10)

        async with self.app.database.session() as session:
            cards = await session.scalars(query)

        if not cards:
            return []

        return [
            Card(
                card_id=card.card_id,
                title=card.title,
                image=card.image,
                price_min=card.price_min,
                price_max=card.price_max,
                genre_title=card.genre_title,
                genre_name=card.genre_name,
                location=card.location,
                address=card.address,
                is_pushkins_card=card.is_pushkins_card,
                details=card.details,
                description=card.description,
            )
            for card in cards.all()
        ]
