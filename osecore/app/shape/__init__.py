"""Exposes functions for the following topological data types or "shapes":

    * compound
    * compsolid
    * solid
    * shell
    * :py:mod:`~osecore.app.shape.face`
    * wire
    * :py:mod:`~osecore.app.shape.edge`
    * vertex

Shape is a generic term covering all of the above.

See Also:
    :freecadwikipage:`Topological data scripting`
"""
from ._move_parts import move_parts
from ._place_shape import place_shape, place_shapes

__all__ = ['move_parts', 'place_shape', 'place_shapes']
