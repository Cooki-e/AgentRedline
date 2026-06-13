"""Notification dispatch."""

from __future__ import annotations

from typing import List, Optional

from .models import User


def queue_email(users: List[User], subject: str) -> List[str]:
    tickets: List[str] = []
    for u in users:
        # cascade-12: Optional[int] in arithmetic / format
        tickets.append(f"mail-{u.id * 31}")
    return tickets
