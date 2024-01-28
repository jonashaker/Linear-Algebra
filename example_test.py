import linear_algebra as la

def example():
    mat = la.Matrix([[1,2,3],[0,1,4],[5,6,0]])
    mat.Print_mat()
    # Output: 1 2 3
    #         1 5 6
    #         1 8 9
    print(mat.Determinant())
    # Output: 0
    mat.Inverse().Print_mat()
    # Output: -0.0 0.0 0.0
    #         0.0 -0.0 0.0
    #         0.0 0.0 -0.0
example()