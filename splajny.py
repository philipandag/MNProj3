import numpy as np

def interpolacja_funkcjami_sklejanymi(X, wezly_x, wezly_y):

    wezly_y = [6, -2, 4]
    wezly_x = [1, 3, 5]


    n = len(wezly_x) - 1
    A = np.zeros((4*n, 4*n))
    b = np.zeros((4*n, 1))


    # S_0''(x_0) = 0, c + 6dh = 0
    h = wezly_x[n] - wezly_x[n-1]
    A[4*n-1][n-1] = 1
    A[4*n-1][n] = 6*h
    b[4*n-1] = 0

    #S_(n-1)''(x_n)=0, c + 6dh = 0
    h = wezly_x[n-1] - wezly_x[n-2]
    A[4*n-2][n-1] = 1
    A[4*n-2][n] = 6*h

    for i in range(n):    # wspolczynniki a_i = f(x_i)
        A[i][4*i] = 1 # a_i
        b[i] = wezly_y[i] # f(x_i)

    for i in range(n):    # wspolczynniki a_i + b_i*h + c_i*h^2 + d_i * h^3 = f(x_(i+1))
        h = wezly_x[i+1]-wezly_x[i]
        A[n+i][4*i] = 1 # a_i
        A[n+i][4*i+1] = h # b_i
        A[n+i][4*i+2] = h**2 # c_i
        A[n+i][4*i+3] = h**3 # d_i
        b[n+i] = wezly_y[i+1] # f(x_(i+1))

    for i in range(n):
        h = wezly_x[i+1]-wezly_x[i]
        A[2*n+i][4*i+1] = 1 # b_i
        A[2*n+i][4*i+2] = 2*h # c_i
        A[2*n+i][4*i+3] = 3*h**2 # d_i

        A[2*n+i][4*i+5] = -1 # b_(i+1)

        b[2*n+i] = 0

    for i in range(n-1):
        h = wezly_x[i+1]-wezly_x[i]
        A[3*n+i][4*i+2] = 2 # c_i
        A[3*n+i][4*i+3] = 6*h # d_i

        A[3*n+i][4*i+6] = -2 # c_(i+1)

    print(A.shape)
    print(b.shape)
    print("det A", np.linalg.det(A))
    x = np.linalg.solve(A, b)

    print("dupa")
    pass





