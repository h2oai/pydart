import json
from typing import Any


def _unwrap(x: dict) -> dict:
    return {k: _unwrap(v._nx_) if hasattr(v, '_nx_') else v for k, v in x.items() if v is not None}


def unwrap(x: Any) -> dict:
    return _unwrap(x._nx_) if hasattr(x, '_nx_') else x


def marshal(x: Any) -> str:
    return json.dumps(unwrap(x), allow_nan=False, separators=(',', ':'))


def unmarshal(s: str) -> dict:
    return json.loads(s)
