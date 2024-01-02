import copy

class Matrix(object):
    """Rectangular table of numbers in the reals."""
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix[0])
        self.columns = len(matrix)


    def _Drop_column(self, column):
        for i in range(self.rows):
            self.matrix[i].pop(column)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
            

    def _Drop_row(self, row):
        self.matrix.pop(row)
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
        
    def Get_column(self, column):
        column_new = []
        for i in range(self.rows):
            column_new.append(self.matrix[i][column])
        return column_new

    def Get_row(self, row):
        return self.matrix[row]

    def Print_mat(self):
        for row in self.matrix:
            print(" ".join(str(number) for number in row))

    def Multiply_by_const(self, c):
        for index, row in enumerate(self.matrix):
            self.matrix[index] = [c*x for x in row]

    def Transpose(self):
        columns_new = self.rows
        rows_new = self.columns
        matrix_new = [[] for _ in range(rows_new)]

        for column in range(self.columns):
            for row in range(self.rows):
                matrix_new[row].append(self.matrix[column][row])

        self.matrix = matrix_new
        self.rows = rows_new
        self.columns = columns_new
            

    def Determinant(self):
        if self.columns == 1:
            #print("hej")
            return self.matrix[0][0]
        else:
            determinant = 0
            for i in range(self.columns):
                matrix_real = copy.deepcopy(self.matrix)
                #print(i, self.matrix[0])
                a_curr = self.matrix[0][i]
                self._Drop_row(0)   
                self._Drop_column(i)
                determinant += (-1)**(i)*a_curr*self.Determinant()
                self.matrix = matrix_real
                self.rows = len(self.matrix)
                self.columns = len(self.matrix[0])
               

        return determinant

    def Invert(self):
        pass

    def Eigenvalues(self):
        pass

    def Diagonalize(self):
        pass

def Identity(size):
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
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    return Matrix(matrix)

        
def Add(A, B):
    new_matrix = []
    for row in range(A.columns):
        new_matrix.append([sum(i) for i in zip(A.matrix[row], B.matrix[row])])

    return Matrix(new_matrix)

def Multiply(A,B):
    matrix = Zeros(A.rows, B.columns)
    



x = Matrix([[-1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x.Determinant())














