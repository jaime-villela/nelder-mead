import numpy as np

class SimplexMatrix:
    """
    A class to symbolize the simplex in the Nelder Mead algorithm.  The method uses the concept of a simplex, 
    which is a special polytope of n + 1 vertices in n dimensions. Examples of simplices include a line segment 
    in one-dimensional space, a triangle in two-dimensional space, a tetrahedron in three-dimensional space, 
    and so forth.

    For this initial example, I am tackling a funciton in two dimensions which means the simplex will be a 
    triangle.

    I'm also taking the liberty of adding a column to the matrix for sorting purposes.  I want to sort the 
    matrix according to the value of the target function at each row.  The WORST row will be the one where
    the value of the function at the values of that row is the greatest.  That is, the values of x,y that
    result in the lowest value of f(x,y) are labeled the BEST row (x,y pair for this example).

    Attributes:
        num_rows (int): number of rows in the matrix
        num_cols (int): number of columns in the matrix
    """

    def __init__(self, num_rows, num_cols):
        """
        Initializes the class with the given attributes.

        Args:
            num_rows (int): number of rows in the matrix
            num_cols (int): number of columns in the matrix
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = np.zeros((num_rows, num_cols+1))
    
    def replace_row_at_index(self, index, new_row):
        """
        Replace a row in the matrix at the specified index.

        Args:
            index (int): The index of the row to replace.
            new_row (list or np.ndarray): The new row to insert.

        Raises:
            ValueError: If the length of the new row does not match the number of columns.
        """
        if len(new_row) != self.num_cols + 1:
            raise ValueError("The length of the new row must match the number of columns in the matrix.")
    
        self.matrix[index] = new_row

    def sort_matrix_by_column(self, column_index):
        """
        Sort the matrix rows based on the values in the specified column.

        Args:
            column_index (int): The index of the column to sort by.

        Raises:
            IndexError: If the column_index is out of bounds.
        """
        if column_index < 0 or column_index >= self.matrix.shape[1]:
            raise IndexError("Column index is out of bounds.")

        # Sort the matrix rows based on the specified column
        self.matrix = self.matrix[self.matrix[:, column_index].argsort()]

    @classmethod
    def create_from_matrix(cls, matrix):
        """
        Create a new SimplexMatrix instance from an existing matrix.

        Args:
            matrix (np.ndarray): A NumPy array representing the simplex.

        Returns:
            SimplexMatrix: A new instance of the SimplexMatrix class.

        Raises:
            ValueError: If the input matrix is not a 2D NumPy array.
        """
        if not isinstance(matrix, np.ndarray):
            raise ValueError("The input must be a NumPy array.")
        if len(matrix.shape) != 2:
            raise ValueError("The input matrix must be two-dimensional.")

        num_rows, num_cols = matrix.shape
        instance = cls(num_rows, num_cols - 1)  # Subtract 1 because the extra column is already included
        instance.matrix = matrix
        return instance


class SimplexTriangle(SimplexMatrix):
    """
    An extension of the simplex where the number of dimesions is 2 which means the simplex is a triangle.
    Since this is a triangle, the matrix represents the three vertices.  Thus, the dimensions are pretty
    much set from the start:  three rows (one for each vertex) and 3 columns (x, y, z - where z is value
    of the function at x,y).

    Attributes:
        num_rows (int): since this is a triangle, 3 rows - one for each vertex
        num_cols (int): since this is in two dimensions, 2 - the extra column is added on init
    """

    # Define constants for indexing rows
    BEST_ROW = 0
    GOOD_ROW = 1
    WORST_ROW = 2

    def __init__(self):
        # Call the parent class constructor
        super().__init__(3, 2)