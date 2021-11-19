import json
from typing import Any


def _unwrap_rec(x: dict) -> dict:
    return {k: _unwrap_rec(v._nx_) if hasattr(v, '_nx_') else v for k, v in x.items() if v is not None}


def _unwrap(x: Any) -> dict:
    return _unwrap_rec(x._nx_) if hasattr(x, '_nx_') else x


def _marshal(x: Any) -> str:
    return json.dumps(x, allow_nan=False, separators=(',', ':'))


def _unmarshal(s: str) -> dict:
    return json.loads(s)


class UI:
    def __init__(self, request: str, on_send):
        self._on_send = on_send
        self._changes = []

    def __setitem__(self, key: str, value: Any):
        self._changes.append((key, _unwrap(value)))

    def __delitem__(self, key: str):
        self._changes.append((key,))

    async def save(self):
        data = _marshal(self._changes)
        self._changes.clear()
        await self._on_send(data)
