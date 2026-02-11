marks = list(map(int, input().split()))

total = sum(marks)
aggregate = (total / 400) * 100

print(total)
print(f"{aggregate:.2f}")

if aggregate > 75:
    print("Distinction")
elif aggregate >= 60:
    print("First Division")
elif aggregate >= 50:
    print("Second Division")
elif aggregate >= 40:
    print("Third Division")
else:
    print("Fail")
