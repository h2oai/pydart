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


def marshal_pretty(x: Any) -> str:
    return json.dumps(x, allow_nan=False, indent=2)


def unmarshal(s: str) -> dict:
    return json.loads(s)
