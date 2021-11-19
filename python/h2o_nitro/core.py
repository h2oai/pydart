import json
from typing import Any


def _dump(xs: Any):
    if isinstance(xs, (list, tuple)):
        return [_dump(x) for x in xs]
    elif isinstance(xs, dict):
        return {k: _dump(v) for k, v in xs.items()}
    elif hasattr(xs, '_nx_'):
        return _dump(xs._nx_)
    else:
        return xs


def _marshal(x: Any) -> str:
    return json.dumps(x, allow_nan=False, separators=(',', ':'))


def _unmarshal(s: str) -> dict:
    return json.loads(s)


class UI:
    def __init__(self, request: str, on_send):
        self._on_send = on_send
        self._changes = []

    def __setitem__(self, key: str, value: Any):
        self._changes.append((key, _dump(value)))

    def __delitem__(self, key: str):
        self._changes.append((key,))

    async def save(self):
        data = _marshal(self._changes)
        self._changes.clear()
        await self._on_send(data)
