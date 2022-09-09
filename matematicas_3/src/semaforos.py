x = 1
y = 0
r = 1
s = 0

processList = []

bufferX = []
bufferY = []
bufferR = []
bufferS = []

def p(_x, _process, _buffer):
    _x -= 1
    if _x < 0:
        _buffer.append(_process)
    return _x

def v(_x, _process, _buffer):
    _x += 1
    if _x <= 0:
        _buffer.remove(_process)
    return _x

# FIRST C
s = p(s,"C",bufferS)
if s >= 0:
    y = p(y, "C", bufferY)
if y > 0:
    x = v(x,"C",bufferX)
    r = v(r,"C",bufferR)

# FIRST B
r = p(r,"B",bufferR)
if r >= 0:
    y = p(y,"B", bufferY)
if y > 0:
    x = v(x,"B", bufferX)
    s = v(s,"B", bufferS)

# FIRST A
x = p(x,"A",bufferX)
"""if x >= 0:
    y = v(y,"A",bufferY)"""

print(f"Value of X is: {x}")
print(f"Value of Y is: {y}")
print(f"Value of R is: {r}")
print(f"Value of S is: {s}")
print(f"List X Contains: {bufferX}")
print(f"List Y Contains: {bufferY}")
print(f"List R Contains: {bufferR}")
print(f"List S Contains: {bufferS}")