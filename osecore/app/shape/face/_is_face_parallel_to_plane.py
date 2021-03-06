import Part
from FreeCAD import Vector


def is_face_parallel_to_xy_plane(face: Part.Face) -> bool:
    """Check if the given face is parallel to the XY plane.

    :param face: A face.
    :type face: Part.Face
    :return: ``True`` if the face is parallel to the XY plane, ``False`` otherwise.
    :rtype: bool
    """
    z_axis = Vector(0, 0, 1)
    return _is_face_parallel_to_plane(face, z_axis)


def is_face_parallel_to_xz_plane(face: Part.Face) -> bool:
    """Check if the given face is parallel to the XZ plane.

    :param face: A face.
    :type face: Part.Face
    :return: ``True`` if the face is parallel to the XZ plane, ``False`` otherwise.
    :rtype: bool
    """
    y_axis = Vector(0, 1, 0)
    return _is_face_parallel_to_plane(face, y_axis)


def is_face_parallel_to_yz_plane(face: Part.Face) -> bool:
    """Check if the given face is parallel to the YZ plane.

    :param face: A face.
    :type face: Part.Face
    :return: ``True`` if the face is parallel to the YZ plane, ``False`` otherwise.
    :rtype: bool
    """
    x_axis = Vector(1, 0, 0)
    return _is_face_parallel_to_plane(face, x_axis)


def _is_face_parallel_to_plane(face, axis_vector):
    return axis_vector == Vector(
        abs(round(face.Surface.Axis.x)),
        abs(round(face.Surface.Axis.y)),
        abs(round(face.Surface.Axis.z))
    )
