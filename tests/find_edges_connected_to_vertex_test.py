import unittest

# Need to import FreeCAD
import FreeCAD as App
import Part

from osecore.app.shape.edge import find_edges_connected_to_vertex


class FindEdgesConnectedToVertexTest(unittest.TestCase):

    def test_freecad(self):
        box = Part.makeBox(10, 10, 10)
        vertex = box.Vertexes[0]

        edges = find_edges_connected_to_vertex(vertex, box.Edges)

        self.assertEqual(len(edges), 3)


if __name__ == '__main__':
    unittest.main()
