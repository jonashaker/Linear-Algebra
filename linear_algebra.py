import copy

class Matrix(object):
    """A class for matrices."""
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix[0])
        self.columns = len(matrix)


    def _Drop_column(self, column):
        """Drops a column from a matrix."""
        for i in range(self.rows):
            self.matrix[i].pop(column)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
            

    def _Drop_row(self, row):
        """Drops a row from a matrix."""
        self.matrix.pop(row)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        
    def _Get_column(self, column):
        """Returns a column of a matrix."""
        column_new = []
        for i in range(self.rows):
            column_new.append(self.matrix[i][column])
        return column_new

    def _Get_row(self, row):
        """Returns a row of a matrix."""
        return self.matrix[row]
    
    def Size(self):
        """Returns the size of a matrix."""
        return (self.rows, self.columns)

    def Print_mat(self):
        """Prints a matrix."""
        for row in self.matrix:
            print(" ".join(str(number) for number in row))

    def Transpose(self):
        """Returns the transpose of a matrix."""
        rows_new = self.columns
        matrix_new = [[] for _ in range(rows_new)]

        for column in range(self.columns):
            for row in range(self.rows):
                matrix_new[row].append(self.matrix[column][row])

        return Matrix(matrix_new)
            

    def Determinant(self):
        """Returns the determinant of a square matrix."""
        # Check if matrix is square
        if self.rows != self.columns:
            raise ValueError("Matrix is not square.")
        # Base case
        if self.columns == 1:
            return self.matrix[0][0]
        # Recursive case
        else:
            determinant = 0
            for i in range(self.columns):
                matrix_real = copy.deepcopy(self.matrix)
                a_curr = self.matrix[0][i]
                self._Drop_row(0)   
                self._Drop_column(i)
                determinant += (-1)**(i)*a_curr*self.Determinant()
                self.matrix = matrix_real
                self.rows = len(self.matrix)
                self.columns = len(self.matrix[0])
        return determinant

    def Inverse(self):
        """Returns the inverse of a matrix."""
        # Check if matrix is square
        if self.rows != self.columns:
            raise ValueError("Matrix is not square.")
        # Check if matrix is invertible
        if self.Determinant() == 0:
            raise ValueError("Matrix is not invertible.")   
        # Cofactor matrix   
        cofactor_matrix = []
        for i in range(self.rows):
            curr_row = []
            for j in range(self.columns):
                matrix_real = copy.deepcopy(self.matrix)
                self._Drop_row(i)
                self._Drop_column(j)
                curr_row.append((-1)**(i+j)*self.Determinant())
                self.matrix = matrix_real
                self.rows = len(self.matrix)
                self.columns = len(self.matrix[0])
            cofactor_matrix.append(curr_row)
        # Adjugate matrix
        adjugate_matrix = []    
        for i in range(self.rows):
            curr_row = []
            for j in range(self.columns):
                curr_row.append(cofactor_matrix[j][i])
            adjugate_matrix.append(curr_row)
        # Inverse matrix
        inverse_matrix = Zeros(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                inverse_matrix.matrix[i][j] = adjugate_matrix[i][j]/self.Determinant()

        return inverse_matrix


def Identity(size):
    """Returns the identity matrix of size n."""
    matrix = []
    for i in range(size):
        curr_row = []
        for j in range(size):
            if i == j:
                curr_row.append(1)
            else:
                curr_row.append(0)
        matrix.append(curr_row)
    return Matrix(matrix)

def Zeros(rows, columns):
    """Returns a matrix of zeros of size m x n."""
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    return Matrix(matrix)

        
def Add(A, B):
    """Adds two matrices."""
    new_matrix = []
    for row in range(A.columns):
        new_matrix.append([sum(i) for i in zip(A.matrix[row], B.matrix[row])])
        
    return Matrix(new_matrix)

def Multiply(A,B):
    """Multiplies two matrices."""
    if A.columns != B.rows:
        raise ValueError("Matrices cannot be multiplied.")
    else:
        new_matrix = []
        for i in range(A.rows):
            curr_row = []
            for j in range(B.columns):
                curr_row.append(sum([x*y for x,y in zip(A._Get_row(i), B._Get_column(j))]))
            new_matrix.append(curr_row)
        return Matrix(new_matrix)
    
def Scalar_multiply(c, A):
    """Multiplies a matrix by a constant."""
    new_matrix = []
    for row in range(A.rows):
        new_matrix.append([c*x for x in A.matrix[row]])
    return Matrix(new_matrix)















