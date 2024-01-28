# Linear Algebra

This library provides basic linear algebra functionalities, allowing for operations on vectors and matrices. It's designed to be simple and user-friendly for small-scale linear algebra computations.

## Documentation
Linear Algebra consists of the following public classes and methods.
### Types
#### Class Matrix

      class Matrix(matrix)
          \\ Creates a matrix object. A rectangular table of real numbers.

#### function Add()
      function Add(A, B) --> Matrix
Returns sum of two matrices.

#### function Scalar_multiply()
      function Scalar_multiply(c, A) --> Matrix
Returns matrix multiplied by constant c.

#### function Zeros()
      function Zeros(rows, columns) --> Matrix
Returns new matrix object with zeros as entries.

#### function Identity()
      function Identity(size) --> Matrix
Returns new matrix object with ones on the main diagonal and zeros everywhere else. 

#### function Transpose()
      function Transpose(A) --> Matrix
Returns new transposed matrix.

#### function Inverse()
      function Inverse(A) --> Matrix
Returns inverse of matrix a.

#### function Determinant()
      function Determinant(A) --> Float
Returns determinant of matrix A.


