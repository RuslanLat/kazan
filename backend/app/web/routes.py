from aiohttp.web_app import Application


def setup_routes(app: Application):
    from app.cards.routes import setup_routes as ship_setup_routes

    ship_setup_routes(app)
