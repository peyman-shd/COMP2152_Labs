# Sample Coding Question 01 Week 01
# Peyman Shahvand

# Question 2: Defining an array (list)
my_array = [1, 4, 7, 9]

# Question 3: Order of Operations
a = 1
b = 2
c = 3
d = 4

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)
print("Question 3 result:", e)
# result: 0

# Question 4: Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))
# The temperature today is: 32.600 degrees Celsius


# Question 5:
userAge = int(input("Enter your age: "))

userAge = userAge + 22
print("Now showing the shop items filtered by age:", userAge)