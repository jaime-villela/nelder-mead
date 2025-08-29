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