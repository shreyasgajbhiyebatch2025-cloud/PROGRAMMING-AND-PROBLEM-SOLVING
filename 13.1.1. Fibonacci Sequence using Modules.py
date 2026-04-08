def generate_fibonacci_sequence(max_value):
	fib_list = [0, 1]
	while True:
		next = fib_list[-1] + fib_list[-2]
		if next > max_value:
			break
		fib_list.append(next)
	return fib_list
