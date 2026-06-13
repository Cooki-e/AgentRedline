"""Text helpers shared by non-export code."""


def normalize_whitespace(value: str) -> str:
    return " ".join(value.split())
