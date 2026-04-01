ph = {}
n = int(input())
for _ in range (n):
	cmd = input().split()
	
	if cmd[0] == "ADD":
		ph[cmd[1]] = cmd[2]

	elif cmd[0] == "REMOVE":
		ph.pop(cmd[1], None)

	elif cmd[0] == "DISPLAY":
		if len(ph) == 0:
			print("No contacts")
		else:
			for name in sorted(ph.keys()):
				print(f"{name}: {ph[name]}")
