class SimplexMatrix:
    """
    A class to symbolize the simplex in the Nelder Mead algorithm.

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

    def get_dimensions(self):
        """
        Simple call to get the matrix dimensions

        Args:
            self (obj): the class itself

        Returns:
            tupple: a combination of the rows and columns in the matrix
        """
        # Method implementation here
        return (self.num_rows, self.num_cols)