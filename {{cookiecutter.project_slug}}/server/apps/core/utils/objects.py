# -*- coding: utf-8 -*-

from functools import reduce
from typing import Optional


def deep_getattr(
    instance: object, attr: str, default: Optional[object] = None,
) -> Optional[object]:
    """Deeping get object attribute."""
    try:
        return reduce(getattr, attr.split("."), instance)
    except AttributeError:
        return default
