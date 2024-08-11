a, b, c = map(int, input().split())
if a==b==c:
    print("Equilateral triangle")
elif a==b!=c or a!=b==c or a==c!=b:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
