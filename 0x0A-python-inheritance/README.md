# 0x0A. Python - Inheritance

## Description

This project consists of several Python scripts and classes that explore the concept of inheritance in object-oriented programming. The tasks involve creating and working with classes, defining methods, and validating attributes.

## Files and Scripts

1. **0-lookup.py**
   - A function `lookup(obj)` that returns a list of available attributes and methods of an object.

2. **1-my_list.py**
   - A class `MyList` that inherits from the `list` class. It includes a method `print_sorted()` that prints the list sorted in ascending order.

3. **2-is_same_class.py**
   - A function `is_same_class(obj, a_class)` that checks if an object is an instance of a specified class.

4. **3-is_kind_of_class.py**
   - A function `is_kind_of_class(obj, a_class)` that checks if an object is an instance of, or inherited from, a specified class.

5. **4-inherits_from.py**
   - A function `inherits_from(obj, a_class)` that checks if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

6. **5-base_geometry.py**
   - An empty class `BaseGeometry` is defined.

7. **6-base_geometry.py**
   - A class `BaseGeometry` is defined with a method `area()` that raises an exception with the message "area() is not implemented."

8. **7-base_geometry.py**
   - A class `BaseGeometry` is defined with an additional method `integer_validator(name, value)` that validates an integer attribute value.

9. **8-rectangle.py**
   - A class `Rectangle` is defined, which inherits from `BaseGeometry`. It includes instantiation with width and height, and an implementation of the `area()` method.

10. **9-rectangle.py**
    - A class `Rectangle` is defined with a `print()` method to print a rectangle description.

11. **10-square.py**
    - A class `Square` is defined that inherits from `Rectangle`. It includes instantiation with size and an implementation of the `area()` method.

12. **11-square.py**
    - A class `Square` is defined with a `print()` method to print a square description.

13. **100-my_int.py**
    - A class `MyInt` is defined, which inherits from `int`. This class has inverted `==` and `!=` operators.

14. **101-add_attribute.py**
    - A function `add_attribute(obj, attribute, value)` that adds a new attribute to an object if possible.

## Requirements

- All Python scripts should be executable and follow PEP 8 style guidelines.
- The first line of each Python script should start with `#!/usr/bin/python3`.
- A README.md file is included at the root of the project folder, providing an overview of the project and descriptions of the scripts and classes.

## Author

This project is authored by Lerato, an ALX student.

Please note that some of the scripts may require you to test them by running the provided test files or by using your own test cases.
