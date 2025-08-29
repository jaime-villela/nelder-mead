import unittest
import numpy as np
from simplex_matrix import SimplexMatrix

class TestSimplexMatrix(unittest.TestCase):
    def test_initialization(self):
        """Test the initialization of SimplexMatrix."""
        num_rows = 3
        num_cols = 4
        simplex = SimplexMatrix(num_rows, num_cols)
        self.assertEqual(simplex.num_rows, num_rows)
        self.assertEqual(simplex.num_cols, num_cols)
        self.assertEqual(simplex.matrix.shape, (num_rows, num_cols+1))
        expected_matrix = [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]]
        self.assertEqual(simplex.matrix.tolist(), expected_matrix)

    def test_replace_row_invalid_length(self):
        """Test replacing a row with an invalid length."""
        num_rows = 3
        num_cols = 4
        simplex = SimplexMatrix(num_rows, num_cols)
        
        # Attempt to replace a row with an invalid length
        new_row = [1, 2, 3]  # Invalid length
        with self.assertRaises(ValueError):
            simplex.replace_row_at_index(0, new_row)

    def test_replace_row(self):
        """Test replacing a row."""
        num_rows = 3
        num_cols = 4
        simplex = SimplexMatrix(num_rows, num_cols)
        
        # Attempt to replace a row with an invalid length
        new_row = [1, 2, 3, 4, 5]
        simplex.replace_row_at_index(0, new_row)
        expected_matrix = [[1, 2, 3, 4, 5],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0]]

        self.assertEqual(simplex.matrix.tolist(), expected_matrix)

    def test_sort_matrix_by_column(self):
        """Test sorting the matrix by a specific column."""
        # Create a SimplexMatrix object
        simplex = SimplexMatrix(3, 2)
        simplex.matrix = np.array([
            [3, 2, 1],
            [1, 3, 2],
            [2, 1, 3]
        ])

        # Sort by the second column (index 1)
        simplex.sort_matrix_by_column(1)

        # Expected result after sorting by column 1
        expected_matrix = np.array([
            [2, 1, 3],
            [3, 2, 1],
            [1, 3, 2]
        ])

        # Assert that the matrix is sorted correctly
        np.testing.assert_array_equal(simplex.matrix, expected_matrix)

    def test_sort_matrix_invalid_column(self):
        """Test sorting with an invalid column index."""
        simplex = SimplexMatrix(3, 2)
        simplex.matrix = np.array([
            [3, 2, 1],
            [1, 3, 2],
            [2, 1, 3]
        ])

        # Attempt to sort by an out-of-bounds column index
        with self.assertRaises(IndexError):
            simplex.sort_matrix_by_column(5)  # Invalid column index

    def test_create_from_matrix(self):
        """Test creating a SimplexMatrix from an existing matrix."""
        # Define an existing matrix
        existing_matrix = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        # Create a SimplexMatrix instance using the from_matrix method
        simplex = SimplexMatrix.create_from_matrix(existing_matrix)

        # Check that the matrix is correctly assigned
        np.testing.assert_array_equal(simplex.matrix, existing_matrix)

        # Check that the number of rows and columns are correctly set
        self.assertEqual(simplex.num_rows, 3)
        self.assertEqual(simplex.num_cols, 2)  # Subtract 1 for the extra column

    def test_create_from_matrix_invalid_input(self):
        """Test creating a SimplexMatrix with invalid input."""
        # Input is not a NumPy array
        with self.assertRaises(ValueError):
            SimplexMatrix.create_from_matrix([[1, 2, 3], [4, 5, 6]])

        # Input is not a 2D array
        with self.assertRaises(ValueError):
            SimplexMatrix.create_from_matrix(np.array([1, 2, 3]))

if __name__ == "__main__":
    unittest.main()