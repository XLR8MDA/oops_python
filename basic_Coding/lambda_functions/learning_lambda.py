''' A lambda function in Python is a small single line function that can take any number of arguments, 
    but can only have one expression. It can be used in place of a function that takes a single expression. 
    It is also used in conjunction with built-in functions like filter(), map() and reduce(). '''


# A lambda function that adds 10 to the number passed in as an argument, and print the result:
x = lambda a : a + 10
print(x(5))

#generally the above function is written as:
def myfunc(a):
    return a+10
print(myfunc(5))


# A lambda function that multiplies argument a with argument b and print the result:
x = lambda a, b : a * b
print(x(5, 6))

#generally the above function is written as:
def myfunc(a,b):
    return a*b
print(myfunc(5,6))

