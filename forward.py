import numpy as np

# emissions matrix
# (just including used probes in order of X for simplicity,
#  actual implementation would have full list of probes and a
#  dictionary to decode to an index within the e matrix)
#  k = 0     1     2
e = [[0.19, 0.23, 0.02],  # N
     [0.28, 0.35, 0.05],  # A
     [0.14, 0.09, 0.31],  # G
     [0.04, 0.11, 0.46]]  # O

# transition matrix
#  k = 0    1    2
a = [[0.5, 0.4, 0.1],  # j = 0
     [0.1, 0.7, 0.2],  # 1
     [0.0, 0.2, 0.8]]  # 2

X = "NAGO"

# initialize forward matrix with start conditions
V = np.zeros((len(e[0]), len(X))).tolist()
V[0][0] = 1.0
# for i in range(1, len(V)):
#     V[i][0] = 0.0

# fill out forward matrix recursively
for i in range(1, len(X)):
    for k in range(len(V)):
        summable = [(a[j][k] * V[j][i-1]) for j in range(k+1)]
        V[k][i] = e[i][k] * np.sum(summable)

prob = np.sum([V[i][len(V[0])-1] for i in range(len(V))])
print(prob)
