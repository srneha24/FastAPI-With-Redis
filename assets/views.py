import aioredis

from .env_vars import REDIS_IP


class Redis:
    __redis_client = None

    def __init__(self) -> None:
        self.__initiate_redis_client()

    def __initiate_redis_client(self):
        self.__redis_client = aioredis.from_url(
            url=f"redis://{REDIS_IP}:6379", encoding="utf-8", decode_responses=True)

    async def create(self, name, value):
        await self.__redis_client.hset(name=name, mapping=value)

    async def retrieve_all(self, name):
        return await self.__redis_client.hgetall(name)

    async def retrive(self, name, key):
        return await self.__redis_client.hget(name, key)
