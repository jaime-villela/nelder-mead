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

if __name__ == "__main__":
    unittest.main()