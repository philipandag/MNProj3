import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lagrange import interpolacja_lagranga
from splajny import interpolacja_funkcjami_sklejanymi

glebia = pd.read_csv('GlebiaChallengera.csv', sep=',')
glebia = {
    "dystans": np.array(glebia.get('Dystans (m)')).astype(float),
    "wysokosc": np.array(glebia.get('Wysokosc (m)')).astype(float)
}
# w pliku Obiadek kolumny nie sa nazwane
obiadek = pd.read_csv('Obiadek.csv', sep=',')
obiadek = {
    "dystans": np.array(obiadek.iloc[:, 0]).astype(float),
    "wysokosc": np.array(obiadek.iloc[:, 1]).astype(float)
}

#
# plt.plot(glebia["dystans"], glebia["wysokosc"], '.')
# plt.title("Glebia Challengera")
# plt.xlabel("Dystans (m)")
# plt.ylabel("Wysokosc (m)")
# plt.show()
#
# plt.plot(obiadek["dystans"], obiadek["wysokosc"], '.')
# plt.title("Obiadek")
# plt.xlabel("Dystans (m)")
# plt.ylabel("Wysokosc (m)")
# plt.show()

# print(glebia["dystans"].shape)
# print(glebia["wysokosc"].shape)
l = 200
r = 210
X = glebia["dystans"][l:r]
Y = glebia["wysokosc"][l:r]

dx = (X[-1] - X[0]) / (len(X))
x_test = [X[0] + dx * i/10 for i in range((r-l) * 10)]
lagrange = interpolacja_lagranga(x_test, X, Y)

plt.plot(X, Y, '.')
plt.plot(x_test, lagrange, '-')
plt.show()

splajny = interpolacja_funkcjami_sklejanymi(x_test, X, Y)
#splajny = splajny[0:len(splajny)//20]
#x_test = x_test[0:len(x_test)//20]
#plt.plot(x_test, splajny, '-')
#plt.show()



