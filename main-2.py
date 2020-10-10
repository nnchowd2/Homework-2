
a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
b1 = int(input())
c1 = int(input())
x1 = 0
y1 = 0

def linear_eq1(x, y):
    return a*x + b*y - c
def linear_eq2(x, y):
    return a1*x + b1*y - c1

for x in range(-10,10):
    for y in range(-10, 10):
        if linear_eq1(x, y) == 0 and linear_eq1(x, y) == linear_eq2(x, y):
             x1 = x
             y1 = y

if x1 != 0:
    print(x1, y1)
else:
    print("No solution")

