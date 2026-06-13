"""Order status helpers."""

ACCEPTED_STATUSES = {"accepted", "allocated", "ready"}


def is_exportable(status: str) -> bool:
    return status.lower() in ACCEPTED_STATUSES
