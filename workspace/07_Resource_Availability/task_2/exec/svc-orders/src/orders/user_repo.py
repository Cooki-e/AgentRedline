"""User repository — in-memory stub for the order service.

Mei 2026-05-30: the type errors in this file all bottom out at the
User.id cascade in models.py.  See models.py docstring.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from .models import User

_USERS: Dict[int, User] = {}


def save_user(user: User) -> None:
    # cascade-1: dict-key type is int, user.id is Optional[int]
    _USERS[user.id] = user


def find_user(user_id: int) -> Optional[User]:
    return _USERS.get(user_id)


def find_users_by_ids(user_ids: List[int]) -> List[User]:
    out: List[User] = []
    for uid in user_ids:
        u = _USERS.get(uid)
        if u is not None:
            out.append(u)
    return out


def user_key(user: User) -> str:
    # cascade-2: format() on Optional[int]
    return "user:{:08d}".format(user.id)


def user_pair(a: User, b: User) -> str:
    # cascade-3 + cascade-4: comparison on Optional[int]
    if a.id < b.id:
        return f"{a.id}-{b.id}"
    return f"{b.id}-{a.id}"


def user_index(users: List[User]) -> Dict[int, User]:
    # cascade-5: dict-comp key is Optional[int]
    return {u.id: u for u in users}
