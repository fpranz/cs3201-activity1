import random

array = []
odd_number = 0
even_number = 0
difference_number = 0

for f in range(10):
  array.append(random.randint(0, 100000000))
print("Random Numbers:", array)

for r in array:
  if (r % 2 == 0):
    even_number += 1
  else:
    odd_number += 1

print("Odd Number:", odd_number)
print("Even Number:", even_number)

difference_number = abs(odd_number - even_number)
print("The difference is:", difference_number)

for r in range(1):
  if even_number > odd_number:
    print("Even is greater than Odd in the array elements")

  elif even_number < odd_number:
    print("Odd is greater than Even in the array elements")

  else:
    print("The Number of Even and Odd on the arrays elements is the same")
