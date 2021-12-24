from utils import readfile

def increases(q):
    tuples = zip(q, q[1:])
    return sum([a < b for a, b in tuples])

s = readfile('day01a.txt')
q = list(map(int, s.split()))
print(increases(q))

windowed = [sum(x) for x in zip(q,q[1:],q[2:])]
print(increases(windowed))
