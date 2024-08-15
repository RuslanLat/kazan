from typing import Optional
import aiohttp_cors
from aiohttp.web import (
    Application as AiohttpApplication,
    Request as AiohttpRequest,
    View as AiohttpView,
)

from aiohttp_apispec import setup_aiohttp_apispec

from app.store.database.database import Database

# from app.store.s3.s3 import S3
from app.store import Store, setup_store
from app.web.logger import setup_logging
from app.web.routes import setup_routes
from app.web.config import Config, setup_config
from app.web.middlewares import setup_middlewares


class Application(AiohttpApplication):
    config: Optional[Config] = None
    store: Optional[Store] = None
    database: Optional[Database] = None
    # s3: Optional[S3] = None


class Request(AiohttpRequest):

    @property
    def app(self) -> Application:
        return super().app()


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request

    @property
    def store(self) -> Store:
        return self.request.app.store

    @property
    def data(self) -> dict:
        return self.request.get("data", {})


app = Application()


def setup_app(config_path: str = None) -> Application:

    setup_logging(app)
    setup_config(app, config_path)
    setup_middlewares(app)
    setup_aiohttp_apispec(
        app,
        title="CARD SERVICE API",
        version="0.0.1",
        swagger_path="/docs",
        url="/docs/json",
    )
    setup_routes(app)
    setup_store(app)
    cors = aiohttp_cors.setup(
        app,
        defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
        },
    )
    for route in list(app.router.routes()):
        cors.add(route)

    return app
