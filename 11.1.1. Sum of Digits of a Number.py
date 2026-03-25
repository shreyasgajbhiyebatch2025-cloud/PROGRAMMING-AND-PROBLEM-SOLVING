num = int(input("Enter a number: "))

sum = 0
while num > 0:
	n = num%10
	sum = sum + n
	num = num//10


print("Sum of digits:",sum)
