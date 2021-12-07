from typing import Any
from .protocol import dump, marshal


class UI:
    def __init__(self, request: str, on_send):
        self._on_send = on_send
        self._changes = []

    def __setitem__(self, key: str, value: Any):
        self._changes.append(('=', key, dump(value)))

    def __delitem__(self, key: str):
        self._changes.append(('~', key))

    async def save(self):
        data = marshal(self._changes)
        self._changes.clear()
        await self._on_send(data)
