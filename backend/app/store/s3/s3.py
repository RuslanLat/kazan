import asyncio
from typing import Any, Optional, TYPE_CHECKING
from miniopy_async import Minio


if TYPE_CHECKING:
    from app.web.app import Application


class S3:
    def __init__(self, app: "Application"):
        self.app: "Application" = app
        self.client: Optional[Minio] = None

    async def connect(self, *_: list, **__: dict) -> None:
        self.client: Minio = Minio(
            self.app.config.s3.host,
            access_key=self.app.config.s3.access_key,
            secret_key=self.app.config.s3.secret_key,
            secure=False,  # http for False, https for True
        )
        self.app.logger.info("S3 подключено")

    async def disconnect(self, *_: Any, **__: Any) -> None:
        try:
            pass
        except:
            pass
        self.app.logger.info("S3 отключено")
