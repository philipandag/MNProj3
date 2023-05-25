import numpy as np


def interpolacja_lagranga(X, wezly_x, wezly_y):
    ret = np.zeros(len(X))
    for x in range(len(X)):
        n = len(wezly_x)
        wynik = 0
        for i in range(n):
            iloczyn = wezly_y[i]
            for j in range(n):
                if i != j:
                    iloczyn *= (X[x] - wezly_x[j]) / (wezly_x[i] - wezly_x[j])
            wynik += iloczyn

        ret[x] = wynik
    return ret