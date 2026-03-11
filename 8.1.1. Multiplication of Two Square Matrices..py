# Read dimension
print("dimension:", end=" ")
n = int(input().strip())


print("first matrix:")
first = []
for _ in range(n):
	row = list(map(int, input().split()))
	first.append(row)


print("second matrix:")
second = []
for _ in range(n):
	row = list(map(int, input().split()))
	second.append(row)


result = [[0] * n for _ in range(n)]


for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j] += first[i][k] * second[k][j]


print("Resultant Matrix:")
for row in result:
	print(*row)





