import typing

from app.cards.views import (
    CardtListView,
)

if typing.TYPE_CHECKING:
    from app.web.app import Application


def setup_routes(app: "Application"):
    app.router.add_view("/cards", CardtListView, name="list_cards")
