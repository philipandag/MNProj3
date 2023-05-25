import numpy as np

def interpolacja_funkcjami_sklejanymi(X, wezly_x, wezly_y, stopien=3):
    parametry = stopien+1
    n = len(wezly_x)

    h = wezly_x[1] - wezly_x[0]


