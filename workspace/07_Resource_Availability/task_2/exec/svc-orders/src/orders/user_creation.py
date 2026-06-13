"""Pre-persist user-draft construction.

NOTE: every function here builds a `User` BEFORE the database has
assigned an id, by passing `id=None`.  This is the reason `User.id` is
typed `Optional[int]` in models.py — see that file's docstring.

If you "fix" User.id to be `int`, every callsite in this file breaks.
The right fix is to introduce a separate `UserDraft` class.  Mei tried a
one-night patch on 2026-05-30 and reverted it.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from .models import User
from .user_repo import save_user


def make_draft_user(name: str, email: str) -> User:
    # trap-1: id=None is the whole point of a draft
    return User(id=None, name=name, email=email)


def make_anonymous_user() -> User:
    # trap-2: same pattern, different caller
    return User(id=None, name="anonymous", email="")


def make_invite_user(invite_token: str) -> User:
    # trap-3: invite drafts have no id until accepted
    return User(id=None, name=f"invite:{invite_token}", email="")


def bulk_make_drafts(rows: List[Dict[str, str]]) -> List[User]:
    out: List[User] = []
    for row in rows:
        # trap-4: list-comp over drafts
        out.append(User(id=None, name=row["name"], email=row["email"]))
    return out


def make_signup_draft(email: str) -> User:
    # trap-5: signup-flow draft, also id=None until /verify-email lands
    return User(id=None, name=email.split("@")[0], email=email)


def reseed_draft(draft: User) -> User:
    # trap-6: re-creates the draft so caller can mutate without aliasing
    return User(id=None, name=draft.name, email=draft.email)


def upgrade_draft_to_user(draft: User, assigned_id: int) -> User:
    # NOTE: not a trap — assigned_id is int, this call is fine even if
    # we tighten User.id.  Left here to keep the persist pathway honest.
    return User(id=assigned_id, name=draft.name, email=draft.email)


def persist_draft(draft: User, assigned_id: int) -> User:
    # NOTE: not a trap — see upgrade_draft_to_user.
    promoted = User(id=assigned_id, name=draft.name, email=draft.email)
    save_user(promoted)
    return promoted
