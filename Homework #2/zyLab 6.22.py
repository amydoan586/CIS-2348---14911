#Amy Doan ID:1895125
# ax + by = c    dx + ey = f
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
for x in range(-10,10):
    for y in range(-10,10):
        line1 = a*x + b*y
        line2 = d*x + e*y
        if (line1 == c and line2 == f):
            print(x,y)
            break

