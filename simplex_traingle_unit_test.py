import unittest
import numpy as np
from simplex_matrix import SimplexTriangle, SimplexMatrix

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

    def test_evaluate_func_at_vertex(self):
        """Test the evaluate_func_at_vertex method."""
        # Define a simple function to test
        def test_function(x, y):
            return x + y

        # Create a SimplexMatrix instance with the test function

        # Initialize the matrix with test values
        sameple_matrix = np.array([
            [1, 2, 0],  # x=1, y=2, z=0 (to be calculated)
            [3, 4, 0],  # x=3, y=4, z=0 (to be calculated)
            [5, 6, 0]   # x=5, y=6, z=0 (to be calculated)
        ])

        simplex = SimplexTriangle.create_from_matrix(sameple_matrix, test_function)

        # Evaluate the function at the first vertex (index 0)
        simplex.evaluate_func_at_vertex(0)

        # Check that the result is correctly stored in the last column
        self.assertEqual(simplex.matrix[0, 2], 3)  # 1 + 2 = 3

        # Evaluate the function at the second vertex (index 1)
        simplex.evaluate_func_at_vertex(1)

        # Check that the result is correctly stored in the last column
        self.assertEqual(simplex.matrix[1, 2], 7)  # 3 + 4 = 7

if __name__ == "__main__":
    unittest.main()