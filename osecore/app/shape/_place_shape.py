from math import degrees
from typing import List

import Part
from FreeCAD import Placement, Vector


def place_shapes(shapes: List[Part.Shape], placement: Placement) -> None:
    """Apply a placement to a given list of shapes.

    See Also:
        https://www.freecadweb.org/api/db/d71/classPart_1_1TopoShapePy.html

    :param shapes: A list of shapes
    :type shapes: List[Part.Shape]
    :param placement: Placement to apply to part
    :type placement: FreeCAD.Placement
    """
    for shape in shapes:
        place_shape(shape, placement)


def place_shape(shape: Part.Shape, placement: Placement) -> None:
    """Apply a placement to a given shape.

    See Also:
        https://www.freecadweb.org/api/db/d71/classPart_1_1TopoShapePy.html

    :param shape: A shape.
    :type shape: Part.Shape
    :param placement: Placement to apply to part
    :type placement: FreeCAD.Placement
    """
    rotation = placement.Rotation
    shape.rotate(Vector(), rotation.Axis, degrees(rotation.Angle))

    translation = placement.Base
    shape.translate(translation)
