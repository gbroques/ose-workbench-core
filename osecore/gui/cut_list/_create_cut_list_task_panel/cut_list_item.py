from typing import NamedTuple


"""TODO: Replace with ``TypedDict`` when no longer support <= Py 3.7.
         See Also:
            https://stackoverflow.com/a/54198204
"""


class CutListItem(NamedTuple):
    """Represents an item in a cut-list.

    Used for typing purposes only.
    """
    quantity: str
    description: str
    length: str
