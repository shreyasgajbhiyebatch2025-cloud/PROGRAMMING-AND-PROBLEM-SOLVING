import string

text = input()
result = ''.join(char for char in text if char.isalnum() or char.isspace())
print(result)
