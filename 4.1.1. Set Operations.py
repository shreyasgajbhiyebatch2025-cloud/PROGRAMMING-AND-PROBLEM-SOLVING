
setA = set(map(int, input("Set A: ").split()))
setB = set(map(int, input("Set B: ").split()))


union_set = setA.union(setB)
intersection_set = setA.intersection(setB)
difference_set = setA.difference(setB)


print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
