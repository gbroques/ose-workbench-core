import Part


def is_face_planar(face: Part.Face) -> bool:
    """Returns whether a face is planar or not.

    Returns ``False`` for cylindrical faces like holes.

    :param face: A face.
    :type face: Part.Face
    :return: ``True`` if the face is planar, ``False`` otherwise.
    :rtype: bool
    """
    return isinstance(face.Surface, Part.Plane)
