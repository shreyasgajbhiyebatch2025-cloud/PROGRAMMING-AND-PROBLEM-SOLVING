class Complex:
	def initComplex(self):# Write the code......
		self.real, self.imag = map(int, input().split())

	def sum(self, c1, c2):
		self.real = c1.real + c2.real
		self.imag = c1.imag + c2.imag

	def display(self):
		if self.imag >= 0:
			print(f"{self.real} + {self.imag}i")
		else:
			print(f"{self.real} - {abs(self.imag)}i")

c1 = Complex()
c2 = Complex()
c3 = Complex()


c1.initComplex()
c2.initComplex()


c3.sum(c1, c2)
c3.display()
