a, b, c = input().split()

digits = [a, b, c]


combinations = [
    digits[0] + digits[1] + digits[2],
    digits[0] + digits[2] + digits[1],
    digits[1] + digits[0] + digits[2],
    digits[1] + digits[2] + digits[0],
    digits[2] + digits[0] + digits[1],
    digits[2] + digits[1] + digits[0]
]


for combo in combinations:
	print(combo)
