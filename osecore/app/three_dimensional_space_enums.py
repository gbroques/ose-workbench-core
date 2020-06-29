"""A set of enumerations relating to three-dimensional space.
"""


class CoordinateAxis:
    """A reference line in a three-dimensional cartesian coordinate system."""
    X = 'x'
    Y = 'y'
    Z = 'z'


class Plane:
    """A plane in a three-dimensional cartesian coordinate system."""
    XY = 'xy'
    YZ = 'yz'
    XZ = 'xz'


class Side:
    """A sides of a three-dimensional object available as one of FreeCAD's standard views.

    See Also:
        :freecadwikipage:`Std View Menu`
    """
    FRONT = 'front'
    TOP = 'top'
    RIGHT = 'right'
    REAR = 'rear'
    BOTTOM = 'bottom'
    LEFT = 'left'


__all__ = [
    'CoordinateAxis',
    'Plane',
    'Side'
]
