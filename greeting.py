"""Greeting helper for the welcome screen (ticket DEMO-1)."""


def greet(name: str) -> str:
    """Return 'Hello, <name>!'. Raises ValueError for an empty name."""
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
