# Problem 1
# Search the list and print whether "banana" is found.
fruits = ["apple", "orange", "banana", "grape"]
if "banana" in fruits:
    print("Found banana")
else:
    print("No banana in list")
# Problem 2
# Count how many numbers are greater than 10 in the list.
numbers = [4, 18, 2, 30, 7, 12]
counter = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 10:
        counter = counter + 1
print(counter, "numbers above 10")


# Problem 3
# Find and print the total sum of all the numbers in the list.
numbers = [4, 11, 22, -6, 3]
print(numbers)

total = sum(numbers)
print("The sum is:", total)


# Problem 4
# Find and print the biggest number in the list.
numbers = [-9, 17, 5, -3, 0]
print(numbers)

biggest_item = max(numbers)


print("The bigest item:", biggest_item)


# Problem 5
# Find and print the sum of only the even numbers in the list. 
numbers = [8, 3, 15, 22, 11, 6]
total = 0
for i in range(len(numbers)):
    item = numbers[i]
    if item > 0:
        total = total + item
print("The sum of only the positive numbers is:", total)