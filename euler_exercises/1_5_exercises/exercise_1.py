print("If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.")
print("Find the sum of all the multiples of 3 or 5 below 1000.")


limit = 1000
index = 1
multiples = 0

while index <= 1000:
  if index % 3 == 0 or index % 5 == 0:
      multiples += index
  index += 1

print("The solution is: " + str(multiples))