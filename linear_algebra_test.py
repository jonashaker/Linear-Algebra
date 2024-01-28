import linear_algebra as la


def test_Size():
    """Tests the Size function."""
    A = la.Matrix([[1,2,3],[4,5,6],[7,8,9]])
    assert A.Size() == (3,3)

def test_add():
    """Tests the Add function."""
    A = la.Matrix([[1,2,3],[4,5,6],[7,8,9]])
    B = la.Matrix([[9,8,7],[6,5,4],[3,2,1]])
    C = la.Matrix([[10,10,10],[10,10,10],[10,10,10]])
    assert la.Add(A,B).matrix == C.matrix

def test_scalar_multiply():
    """Tests the scalar_multiply function."""
    A = la.Matrix([[1,2,3],[4,5,6],[7,8,9]])
    B = la.Matrix([[2,4,6],[8,10,12],[14,16,18]])
    assert la.scalar_multiply(2,A).matrix == B.matrix

def test_multiply():
    """Tests the Multiply function."""
    A = la.Matrix([[1,2,3],[4,5,6],[7,8,9]])
    B = la.Matrix([[1,2,3],[4,5,6],[7,8,9]])
    C = la.Matrix([[30,36,42],[66,81,96],[102,126,150]])
    assert la.Multiply(A,B).matrix == C.matrix

def test_zeros():
    """Tests the Zeros function."""
    A = la.Zeros(3,3)
    B = la.Matrix([[0,0,0],[0,0,0],[0,0,0]])
    assert A.matrix == B.matrix

def test_identity():
    """Tests the Identity function."""
    A = la.Identity(3)
    B = la.Matrix([[1,0,0],[0,1,0],[0,0,1]])
    assert A.matrix == B.matrix

def test_transpose():
    """Tests the Transpose function."""
    A = la.Matrix([[1,2,3],[4,5,6],[7,8,9]])
    B = la.Matrix([[1,4,7],[2,5,8],[3,6,9]])
    assert A.Transpose().matrix == B.matrix

def test_inverse():
    """Tests the Inverse function."""
    A = la.Matrix([[1,2,3],[0,1,4],[5,6,0]])
    B = la.Matrix([[-24,18,5],[20,-15,-4],[-5,4,1]])
    assert A.Inverse().matrix == B.matrix

def test_determinant():
    """Tests the Determinant function."""
    A = la.Matrix([[1,2,3],[0,1,4],[5,6,0]])
    assert A.Determinant() == 1


def main():
    test_Size()
    test_add()
    test_scalar_multiply()
    test_multiply()
    test_zeros()
    test_identity()
    test_transpose()
    test_inverse()
    test_determinant()
    print("All tests passed.")

if __name__ == '__main__':
    main()


