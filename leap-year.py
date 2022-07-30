



# Exercise | ?comprehension | ?range() | ?len() | ?nested for loop() | ?any() | ?sum() | ?append()**
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number which  is evenly divisible by all of the numbers from 1 to 20?
# MClay
nums_prime = []

for i in nums :
  prime = []
  for j in range(2,i) :
    prime.append(i % j != 0)
  if all(prime) and i != 1 :
    nums_prime += [i]
new_number = []
while True :
  for i in nums_prime :
    temp = []
    for j in range(len(nums)) :
      temp.append(nums[j] % i == 0)
      if nums[j] % i == 0 :
        nums[j] = nums[j] // i
    if any(temp) :
      new_number += [i]
  if sum(nums) == 20 :
    break
count = 1    
for i in new_number :
  count *= i
print(count)
# Default function to implement conditions to check leap year  
def CheckLeap(year) :  
  # Checking if the given year is leap year  


print("merhaba")


x = 6

while x < 15:
	print(x)
	x += 1



print("saık erdemmir")


print(b)




x = 6

while x < 15:
	print(x)
	x += 1


#code bug control



print("All rights are reserved")


print(b)
print("Hello Cohort-12")


print(b)
print("Hello Cohort-12")

print("MErhabalar")


print(b)

<<<<<<< HEAD
print("Hello Cohort-12")

print("Buraya bakarlar")

print ("merhaba")

print("Hello Cohort-12

x = 6

while x < 15:
	print(x)
	x += 1
print("Hahahaha")


print("have nice holiday")

print("yavaş öğreniyorum galiba")
