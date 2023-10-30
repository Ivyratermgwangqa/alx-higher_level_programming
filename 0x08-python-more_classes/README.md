# 0x08. Python - More Classes and Objects

## Overview

This repository contains Python programs and scripts that demonstrate the use of classes and objects. The tasks cover various aspects of object-oriented programming, including attributes, methods, class attributes, and special methods.

## Task List

### 0. Simple Rectangle (0-rectangle.py)
- Define an empty class `Rectangle` representing a rectangle.

### 1. Real Definition of a Rectangle (1-rectangle.py)
- Define a class `Rectangle` with private instance attributes `width` and `height`.
- Implement property setters and getters for `width` and `height`.
- Initialize `width` and `height` in the constructor.

### 2. Area and Perimeter (2-rectangle.py)
- Enhance the `Rectangle` class by adding public methods to calculate the area and perimeter.
- Implement checks for valid dimensions (width and height) in property setters.

### 3. String Representation (3-rectangle.py)
- Improve the `Rectangle` class to display the rectangle using the '#' character.
- Implement special methods `__str__` and `__repr__` for a more readable representation.

### 4. Eval is Magic (4-rectangle.py)
- Extend the `Rectangle` class to support recreation using `eval()`.
- Define a class method `def new(cls, width, height):` to create a new instance.

### 5. Detect Instance Deletion (5-rectangle.py)
- Add a special method `__del__` to the `Rectangle` class.
- When an instance is deleted, it should print "Bye rectangle..." (three dots).

### 6. How Many Instances (6-rectangle.py)
- Add a class attribute `number_of_instances` to count the number of `Rectangle` instances created.
- Increment and decrement this count when instances are created and deleted.

### 7. Change Representation (7-rectangle.py)
- Introduce a public class attribute `print_symbol` to customize the representation character (default is '#').
- Update the `__str__` method to use the `print_symbol`.

### 8. Compare Rectangles (8-rectangle.py)
- Implement a static method `def bigger_or_equal(rect_1, rect_2):` in the `Rectangle` class.
- It should return the rectangle with the greater area or `rect_1` if both rectangles have the same area.

### 9. A Square is a Rectangle (9-rectangle.py)
- Create a new class method `def square(cls, size=0):` in the `Rectangle` class.
- It should create a new instance with equal width and height, effectively representing a square.

### 10. N Queens (101-nqueens.py)
- Implement a program to solve the N queens puzzle using backtracking.
- The program takes an integer N as a command-line argument and prints all possible solutions on the chessboard.

### 11. CPython #1: PyBytesObject (102-magic_string.py)
- Create a class `MyString` that inherits from the `str` class.
- Implement comparison methods for length comparisons such as `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, and `__ge__`.

## Usage

To run each task, create a Python script and import the corresponding class or function. For Task 10, use the command line as follows:

```bash
$ ./101-nqueens.py N
```

Replace N with the desired board size.

## Author

This repository is maintained by an AI language model as part of an educational project.

You can find more information about [OpenAI](https://openai.com) and [GPT-3](https://openai.com/gpt-3/).

For questions or feedback, please contact Ivyratermgwangqa.

## Disclaimer

This is a simple educational project, and the code may not be suitable for production use. It is provided as a reference and learning resource.
