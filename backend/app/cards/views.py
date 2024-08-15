from typing import List, Optional
from aiohttp.web import Response, HTTPFound
from aiohttp_apispec import (
    docs,
    request_schema,
    response_schema,
)
from aiohttp_cors import CorsViewMixin

from app.web.app import View
from app.web.utils import json_response
from app.cards.schemes import (
    CardListResponseSchema,
)
from app.cards.models import Card


class CardtListView(View, CorsViewMixin):  # AuthRequiredMixin,
    @response_schema(CardListResponseSchema, 200)
    @docs(
        tags=["cards"],
        summary="Add cards list view",
        description="Get list cards from database",
    )
    async def get(self) -> Response:
        cards: List[Optional[Card]] = await self.store.cards.list_cards()
        return json_response(CardListResponseSchema().dump({"cards": cards}))


# class ImgShipView(View):
#     async def get(self):

#         file_name: str = self.request.match_info["file_name"]

#         url = await self.store.s3.url_get_object(
#             bucket_name="ships", file_name=file_name
#         )

#         raise HTTPFound(url)
