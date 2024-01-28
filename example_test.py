import linear_algebra as la

def example():
    mat = la.Matrix([[1,2,3],[0,1,4],[5,6,0]])
    mat.Print_mat()
    # Output: 1 2 3
    #         0 1 4
    #         5 6 0
    print(mat.Determinant())
    # Output: 1
    mat.Inverse().Print_mat()
    # Output: -24.0 18.0 5.0
    #         20.0 -15.0 -4.0
    #          -5.0 4.0 1.0