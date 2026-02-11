import math

a, b, c = map(int, input().split())
D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"root1 = {root1:.2f}")
    print(f"root2 = {root2:.2f}")
elif D == 0:
    root = -b / (2*a)
    print(f"root1 = root2 = {root:.2f}")
else:
    real = -b / (2*a)
    imag = math.sqrt(-D) / (2*a)
    print(f"root1 = {real:.2f}+{imag:.2f}i")
    print(f"root2 = {real:.2f}-{imag:.2f}i")




