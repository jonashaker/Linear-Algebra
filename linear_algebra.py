class Matrix:
    """Rectangular table of numbers in the reals."""
    def __init__(self, matrix):
        self.matrix = matrix
        self.columns = len(matrix)
        self.rows = len(matrix[0])

    def Print_mat(self):
        for row in self.matrix:
            print(" ".join(str(number) for number in row))

    def Multiply_by_const(self, c):
        for row in self.matrix:

    def Determinant(self):
        pass

    def Invert(self):
        pass

    def Transpose(self):
        pass
    
    def Eigenvalues(self):
        pass
    

    def Diagonalize(self):
        pass


            

def Add(A, B):
    pass

def Multiply(A,B):
    pass





x = Matrix([[1,2], [3,4]])
x.print_mat()


