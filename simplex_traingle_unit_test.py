import unittest
import numpy as np
from simplex_matrix import SimplexTriangle

class TestSimplexTriangle(unittest.TestCase):
    def test_initialization(self):
        """Test the initialization of the SimplexTriangle."""
        triangle = SimplexTriangle()
        
        # Check the dimensions of the matrix
        self.assertEqual(triangle.num_rows, 3)
        self.assertEqual(triangle.num_cols, 2)
        self.assertEqual(triangle.matrix.shape, (3, 3))  # 3 rows, 3 columns (2 + 1)

        # Check default values in the matrix
        expected_matrix = np.zeros((3, 3))
        np.testing.assert_array_equal(triangle.matrix, expected_matrix)

    def test_constants(self):
        """Test the constants for row indexing."""
        self.assertEqual(SimplexTriangle.BEST_ROW, 0)
        self.assertEqual(SimplexTriangle.GOOD_ROW, 1)
        self.assertEqual(SimplexTriangle.WORST_ROW, 2)

    def test_replace_row(self):
        """Test replacing a row in the SimplexTriangle."""
        triangle = SimplexTriangle()
        
        # Replace the BEST_ROW
        new_row = [1, 2, 3]
        triangle.replace_row_at_index(SimplexTriangle.BEST_ROW, new_row)
        
        # Verify the row was replaced
        self.assertTrue(np.array_equal(triangle.matrix[SimplexTriangle.BEST_ROW], new_row))

        # Verify other rows remain unchanged
        self.assertTrue(np.array_equal(triangle.matrix[SimplexTriangle.GOOD_ROW], [0, 0, 0]))
        self.assertTrue(np.array_equal(triangle.matrix[SimplexTriangle.WORST_ROW], [0, 0, 0]))

if __name__ == "__main__":
    unittest.main()