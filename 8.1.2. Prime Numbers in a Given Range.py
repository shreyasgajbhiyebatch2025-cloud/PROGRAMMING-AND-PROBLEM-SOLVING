
start = int(input())
end = int(input())


def is_prime(num):
	if num < 2:
		return False
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			return False
	return True


primes = [str(i) for i in range(start, end + 1) if is_prime(i)]


if primes:
	print("\n".join(primes))
else:
	print("No primes")

