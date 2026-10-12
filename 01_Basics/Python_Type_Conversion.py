# What is type conversion?
# Type conversion means changing a value from one data type to another.
# Imagine you ask someone their age. They type 25. Python's input() function receives the answer as text, not automatically as an integer.

# Important conversion functions
# Function	Converts to	Example	Result
# int()	Integer	int("25")	25
# float()	Float	float("3.5")	3.5
# str()	String	str(100)	"100"
# bool()	Boolean	bool(1)	True
# list()	List	list("cat")	['c', 'a', 't']
# tuple()	Tuple	tuple([1, 2])	(1, 2)
# set()	Set	set([1, 1, 2])	{1, 2}
# Let's practise the most important ones.


age = int("25")

print(age + 5)



price = float("19.99")

print(price + 5)



age = 25

message = "My age is " + str(age)

print(message)



print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))


# A useful rule:
# - 0, "", [], and None are false-like values.
# - Non-empty strings and non-zero numbers are generally true-like.
# One important detail: bool("False") returns True, because "False" is a non-empty string. Python does not interpret that text as the Boolean value False.