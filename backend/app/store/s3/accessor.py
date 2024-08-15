from app.base.base_accessor import BaseAccessor


class S3Accessor(BaseAccessor):

    async def create_file(
        self, bucket_name: str, file_name: str, data: bytes, part_size: int
    ) -> None:

        await self.app.s3.client.put_object(
            bucket_name=bucket_name,
            object_name=file_name,
            data=data,
            length=-1,
            part_size=part_size,
        )

    async def create_bucket(self, bucket_name: str) -> None:

        await self.app.s3.client.make_bucket(bucket_name=bucket_name)

    async def url_get_object(self, bucket_name: str, file_name: str):

        url = await self.app.s3.client.presigned_get_object(
            bucket_name=bucket_name, object_name=file_name
        )

        return url
