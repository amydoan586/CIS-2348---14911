#Amy Doan ID:1895125
# ax + by = c    dx + ey = f
a = int(input()) # variable for x for line 1
b = int(input()) # variable for y for line 1
c = int(input())
d = int(input()) # variable for x for line 2
e = int(input()) # variable for y for line 1
f = int(input())
solution = False
for x in range(-10,10):
    for y in range(-10,10):
        line1 = a*x + b*y
        line2 = d*x + e*y
        if (line1 == c and line2 == f):
            print(x,y)
            solution = True
if not solution: # Solution must be false to print No solution
    print("No solution")
