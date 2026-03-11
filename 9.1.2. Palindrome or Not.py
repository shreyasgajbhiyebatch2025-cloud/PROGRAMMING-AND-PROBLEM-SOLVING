st = input()
flag = 1
n = len(st)

for i in range (n // 2):
	if st[i] !=st[n - i - 1]:
		flag = 0
		break 
if flag == 1:
	print("Palindrome")
else:
	print("Not a Palindrome")
