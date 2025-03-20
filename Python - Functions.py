# len() function in Python returns the number of items/elements in an object such as list, tuple etc
# example of len() function
list1 = [2,8,9,10,24,7]
print("Length of list: ", len(list1))

# a Python function greet(name) that takes a person's name as input and prints "Hello, [name]!."
name = input("Enter the name :")
def greet(name):
     print(f"Hello, {name}!")
           
greet(name)

# a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values.
def find_maximum(numbers):
        max = numbers[0]
        for i in numbers:
           if( i > max):
               max = i
        return max

numbers = [10,20,30,40,50,60]
largest_number = find_maximum(numbers)
print("Largest number is: ", largest_number)


# Explain the difference between local and global variables in a Python function.
# Global variables : are defined outside any function and can be accessed anywhere in the program. If we want to modify a global variable inside a function, we must explicitly declare it using the global keyword.
# Local variables : are defined inside a function and can only be accessed inside that function. If a local variable has same name as a global variable, changes made in the local variable will not affect the global variable of same name.

# example and explanation of local and global variables
# a program where a global variable and a local variable have the same name and show how Python differentiates between them.
n = 10          # global variable
def sample():
       n = 5       # local variable with the same name as global variable. Assigning n as 5 will not affect the global variable value 
       print("Inside function - local variable = ", n)       # output as 5 

sample()
print("Outside function - global variable = ", n)        # output as 10 ( global variable value remains unchanged )


      
# a function calculate_area(length, width=5) that calculates the area of a rectangle. 
# If only the length is provided, the function should assume the width is 5. 
# Show how the function behaves when called with and without the width argument.
def calculate_area(length, width=5):
       return length*width

print("Area of rectangle (without width argument): ", calculate_area(10))        # default width is taken as 5
print("Area of rectangle (with width argument): ", calculate_area(10,20))        # here width is taken as 20 which is the argument being passed 