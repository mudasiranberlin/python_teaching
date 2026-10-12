# Rules for naming variables
# Valid variable names:
name = "Ali"
student_age = 20
price2 = 50
_private = "example"

# Invalid variable names:

# 2name = "Ali"     # Cannot start with a number
# student-age = 20  # Hyphen is not allowed
# class = "Python"  # Reserved keyword

# Use meaningful names such as student_age, total_price, and server_ip rather than confusing names such as x1 when a clearer name is possible.

# More than one variable at a time

# Python supports multiple assignment:

name, age, country = "Mudasir", 25, "Cambodia"

print(name)
print(age)
print(country)

# It also supports assigning the same value to multiple variables:

x = y = z = 10

