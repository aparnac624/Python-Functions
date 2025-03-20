{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "78cdf533-7eb3-40d2-b792-47696be0adce",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Length of list: 6\n"
     ]
    }
   ],
   "source": [
    "# len() function in Python returns the number of items/elements in an object such as list, tuple etc\n",
    "# example of len()\n",
    "list1 = [2,8,9,10,24,7]\n",
    "print(\"Length of list:\", len(list1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "419430ec-c063-41fa-b36c-49b8b4c2239e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the name : Aparna\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Aparna!\n"
     ]
    }
   ],
   "source": [
    "# a Python function greet(name) that takes a person's name as input and prints \"Hello, [name]!\".\n",
    "name = input(\"Enter the name :\")\n",
    "def greet(name):\n",
    "    print(f\"Hello, {name}!\")\n",
    "    \n",
    "greet(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8eb66435-2e9e-4680-81fc-f0752261ee73",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest number is: 60\n"
     ]
    }
   ],
   "source": [
    "# a Python function find_maximum(numbers) that takes a list of integers and returns the maximum value without using the built-in max() function. \n",
    "# Use a loop to iterate through the list and compare values. \n",
    "def find_maximum(numbers):\n",
    "    max = numbers[0]\n",
    "    for i in numbers:\n",
    "        if( i > max):\n",
    "            max = i\n",
    "    return max\n",
    "\n",
    "numbers = [10,20,30,40,50,60]\n",
    "largest_number = find_maximum(numbers)\n",
    "print(\"Largest number is:\", largest_number)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f76a74f0-b589-4e68-aab6-0d3fe1a2cf8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Explain the difference between local and global variables in a Python function.\n",
    "# Global variables : are defined outside any function and can be accessed anywhere in the program. If we want to modify a global variable inside a function, we must explicitly declare it using the global keyword.\n",
    "# Local variables : are defined inside a function and can only be accessed inside that function. If a local variable has same name as a global variable, changes made in the local variable will not affect the global variable of same name."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6481c54f-0408-46cf-a6f1-12b97cfb9687",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inside function - local variable =  5\n",
      "Outside function - global variable =  10\n"
     ]
    }
   ],
   "source": [
    "# example and explanation of local and global variables\n",
    "# a program where a global variable and a local variable have the same name and show how Python differentiates between them. \n",
    "\n",
    "n = 10          # global variable\n",
    "def sample():\n",
    "    n = 5       # local variable with the same name as global variable. Assigning n as 5 will not affect the global variable value \n",
    "    print(\"Inside function - local variable = \", n)       # output as 5 \n",
    "\n",
    "sample()\n",
    "print(\"Outside function - global variable = \", n)        # output as 10 ( global variable value remains unchanged )\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "89f57cc1-6329-470e-9712-22aebc13525f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area of rectangle (without width argument):  50\n",
      "Area of rectangle (with width argument):  200\n"
     ]
    }
   ],
   "source": [
    "# a function calculate_area(length, width=5) that calculates the area of a rectangle. \n",
    "# If only the length is provided, the function should assume the width is 5. \n",
    "# Show how the function behaves when called with and without the width argument. \n",
    "\n",
    "def calculate_area(length, width=5):\n",
    "    return length*width\n",
    "\n",
    "print(\"Area of rectangle (without width argument): \", calculate_area(10))        # default width is taken as 5\n",
    "print(\"Area of rectangle (with width argument): \", calculate_area(10,20))        # here width is taken as 20 which is the argument being passed \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b51e204-3509-4993-ab48-dff7899f0466",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
