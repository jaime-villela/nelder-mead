import unittest
from simplex_matrix import SimplexMatrix

class TestSimplexMatrix(unittest.TestCase):
    def test_initialization(self):
        """Test the initialization of SimplexMatrix."""
        num_rows = 3
        num_cols = 4
        simplex = SimplexMatrix(num_rows, num_cols)
        self.assertEqual(simplex.num_rows, num_rows)
        self.assertEqual(simplex.num_cols, num_cols)

    def test_get_dimensions(self):
        """Test the get_dimensions method."""
        num_rows = 3
        num_cols = 4
        simplex = SimplexMatrix(num_rows, num_cols)
        dimensions = simplex.get_dimensions()
        self.assertEqual(dimensions, (num_rows, num_cols))

if __name__ == "__main__":
    unittest.main()