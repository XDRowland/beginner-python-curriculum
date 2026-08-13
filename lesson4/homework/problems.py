import random


# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
ops = ["Windows", "macOS", "Linux"]

# Print the last one using len()
print("Last OS:", ops[len(ops) - 1])

# Reverse the list and print it
ops.reverse()
print("Reversed list:", ops)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["Math", "History", "Science", "English"]

# Print the second subject (index 1)
print("Second subject:", subjects[1])

# Sort alphabetically and print
subjects.sort()
print("Sorted subjects:", subjects)


# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
error_codes = [404, 500, 403, 400, 502]

# Print how many there are
print("Number of error codes:", len(error_codes))

# Use a for loop to print each error code
for code in error_codes:
    print(code)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
languages = ["Python", "JavaScript"]

# Print a random language
print("Random language:", random.choice(languages))

# Append another language and print the list
languages.append("C++")
print("Updated languages:", languages)



# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["p@ss1", "secret123", "admin2026", "qwerty89", "letmein!", "safeP@ss"]

# For an even length list (6 items), index len() // 2 gives the start of the middle section (index 3)
middle_index = len(passwords) // 2
print("Middle password:", passwords[middle_index])

# Remove the first password and print the list
passwords.pop(0)  # or del passwords[0] / passwords.remove(passwords[0])
print("List after removing the first password:", passwords)