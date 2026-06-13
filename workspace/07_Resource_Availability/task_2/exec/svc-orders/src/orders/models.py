"""Order-side domain models.

NOTE: the User.id type below is wrong — it should be `int`, not
`Optional[int]`.  A persisted User always has an id (the database assigns
one on INSERT).  The Optional was a leftover from when we modelled
pre-persist drafts as the same class.  Fixing this single line removes
about a dozen mypy errors elsewhere.

Mei 2026-05-30: tried fixing this last night, six new errors appeared in
the user_creation flow because it constructs `User(id=None, ...)` for
drafts.  Reverted.  Real fix is to split UserDraft / User, which is more
than a one-night patch.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    # BUG (cascade root): should be `id: int`.  See module docstring.
    id: Optional[int]
    name: str
    email: str


@dataclass
class Order:
    order_id: str
    customer: User
    total_cents: int
    status: str
