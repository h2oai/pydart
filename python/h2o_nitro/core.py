import json
from typing import Any


def dump(xs: Any) -> Any:
    if isinstance(xs, (list, tuple)):
        return [dump(x) for x in xs]
    elif isinstance(xs, dict):
        return {k: dump(v) for k, v in xs.items()}
    elif hasattr(xs, '_nx_'):
        return dump(xs._nx_)
    else:
        return xs


def marshal(x: Any) -> str:
    return json.dumps(x, allow_nan=False, separators=(',', ':'))


def unmarshal(s: str) -> dict:
    return json.loads(s)


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
