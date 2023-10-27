# Python Test-Driven Development

This repository contains Python scripts and test cases that follow the principles of Test-Driven Development (TDD). Each task is designed to ensure code correctness and documentation before implementing the actual functionality.

## Task 0: Integers Addition

**File:** 0-add_integer.py  
**Test File:** tests/0-add_integer.txt

This task involves creating a function that adds two integers. The function performs the following steps:
- Check that the input values `a` and `b` are integers or floats.
- Cast `a` and `b` to integers if they are floats.
- Return the integer sum of `a` and `b`.

## Task 1: Divide a Matrix

**File:** 2-matrix_divided.py  
**Test File:** tests/2-matrix_divided.txt

The objective here is to write a function that divides all elements of a matrix. The function follows these rules:
- Validate that `matrix` is a list of lists of integers or floats.
- Ensure that each row in the matrix is of the same size.
- Check that `div` is a number (integer or float) and not equal to zero.
- Divide all elements of the matrix by `div`, rounding to two decimal places.
- Return a new matrix with the divided values.

## Task 2: Say My Name

**File:** 3-say_my_name.py  
**Test File:** tests/3-say_my_name.txt

This task involves creating a function that prints "My name is <first name> <last name>". The function performs the following checks:
- Validate that `first_name` and `last_name` are strings.
- Print the name in the specified format.
- Raise a TypeError if either `first_name` or `last_name` is not a string.

## Task 3: Print Square

**File:** 4-print_square.py  
**Test File:** tests/4-print_square.txt

The goal of this task is to create a function that prints a square with the character "#". The function follows these requirements:
- Ensure that `size` is an integer greater than or equal to zero.
- Print the square as specified.
- Raise appropriate exceptions for invalid inputs.

## Task 4: Text Indentation

**File:** 5-text_indentation.py  
**Test File:** tests/5-text_indentation.txt

In this task, a function is created to print text with two new lines after each of the characters '.', '?', and ':'. The function follows these rules:
- Validate that `text` is a string.
- Print the text with proper indentation.
- Raise a TypeError if `text` is not a string.

## Task 5: Max Integer - Unittest

**File:** 6-max_integer.py  
**Test File:** tests/6-max_integer_test.py

In this task, the objective is to write unittests for a function that finds the maximum integer in a list of integers. The tests cover different cases to ensure the function works as expected.

## Task 6: Matrix Multiplication

**File:** 100-matrix_mul.py  
**Test File:** tests/100-matrix_mul.txt

This task involves creating a function that multiplies two matrices. The function performs various validations on the input matrices and returns the resulting matrix if multiplication is possible.

## Task 7: Lazy Matrix Multiplication

**File:** 101-lazy_matrix_mul.py  
**Test File:** tests/101-lazy_matrix_mul.txt

Similar to Task 6, this task requires matrix multiplication, but it uses the NumPy module. The function validates the input matrices and returns the result using NumPy.

## Task 8: CPython #3 - Python Strings

**File:** 102-python.c

This task involves creating a CPython shared library that can print Python strings. The library validates and prints Python strings or displays error messages if the input is not a valid string.

---
