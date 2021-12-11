import json
import inspect
from typing import Any, Callable, Dict, List, Tuple, Optional, Awaitable

ChangeSet = List[Optional[
    Tuple[str, str],
    Tuple[str, str, Any],
]]

Delegate = Callable[['UI'], Awaitable[None]]
Send = Callable[[str], Awaitable[None]]


def _marshal(x: Any):
    return json.dumps(x, allow_nan=False, separators=(',', ':'))


def _fqn(x: Any):
    return f'{x.__module__}.{x.__name__}' if hasattr(x, '__name__') and hasattr(x, '__module__') else ''


class _GUID:
    def __init__(self):
        self._id: int = 0

    def read(self):
        self._id += 1
        return str(self._id)


class _DispatchTable:
    def __init__(self):
        self._guid = _GUID()
        self._guids: Dict[str, Delegate] = {}
        self._delegates: Dict[Delegate, str] = {}

    def add(self, d: Delegate) -> str:
        if d in self._delegates:
            return self._delegates[d]
        guid = self._guid.read()
        self._delegates[d] = guid
        self._guids[guid] = d
        return guid

    def lookup(self, guid: str) -> Delegate:
        return self._guids.get(guid, None)


def _dump(d: _DispatchTable, xs: Any) -> Any:
    if isinstance(xs, (list, tuple)):
        return [_dump(d, x) for x in xs]
    elif isinstance(xs, dict):
        return {k: _dump(d, v) for k, v in xs.items()}
    elif hasattr(xs, '_nx_'):
        return _dump(d, xs._nx_)
    elif inspect.isfunction(xs):
        if inspect.iscoroutinefunction(xs):
            return {'f': d.add(xs)}
        else:
            raise ValueError(f'dump failed: want async function, got non-async: {_fqn(xs)}() ')
    else:
        return xs


class Nitro:
    def __init__(self, on_load: Delegate):
        self.dispatch_table = _DispatchTable()
        self._on_load = on_load

    async def load(self, send: Send, **context):
        self._on_load(UI(self, send, context))

    async def handle(self, request: str, send: Send, **context):
        r = json.loads(request)
        if isinstance(r, dict):
            guid = r.get('f', None)
            if guid is not None:
                d = self.dispatch_table.lookup(guid)
                await d(UI(self, send, context))  # TODO pass event args


class UI:
    def __init__(self, nitro: Nitro, send: Send, context: dict):
        self._nitro = nitro
        self._send = send
        self._changes: ChangeSet = []
        for k, v in context.items():
            setattr(self, k, v)

    def __setitem__(self, key: str, value: Any):
        self._changes.append(('=', key, _dump(self._nitro.dispatch_table, value)))

    def __delitem__(self, key: str):
        self._changes.append(('~', key))

    async def save(self):
        changes = _marshal(self._changes)
        self._changes.clear()
        await self._send(changes)
