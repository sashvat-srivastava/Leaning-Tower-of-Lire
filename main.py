import numpy as np

M = 1
L = 1

def com_sequence(n):
    xs = np.array([L/2])
    coms = np.array([L/2])
    m = M
    mx = M*xs[0]

    for k in range(2, n+1):
        new_x = (mx/m) + L/2
        xs = np.append(xs, new_x)
        mx += M*new_x
        m += M
        coms = np.append(coms, mx/m)
    return coms, xs

n = int(input("Enter number of blocks: "))

coms, xs = com_sequence(n)
print("COMs:\n", coms)
print("Block centers:\n", xs)

overhangs = np.diff(coms, prepend=L/2)
overhangs[0] = L/2
print("Individual overhangs:\n", overhangs)

def HarmonicSeries(n):
    return 1/np.arange(1, n+1)

HS = HarmonicSeries(n)
print("Harmonic Series:\n", HS)
WHS = (L/2)*HS
print("Weighted Harmonic Series:\n", WHS)

diff = np.zeros(n)
for i in range(n):
    diff[i] = abs(WHS[i] - overhangs[i])

s = 0
for i in range(n):
    s += abs(diff[i])

print("absolute error:\n", s/n)