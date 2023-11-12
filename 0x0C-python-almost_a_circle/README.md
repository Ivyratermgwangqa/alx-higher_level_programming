# README.md - Almost a Circle Project

## Project Overview

This project is part of the ALX Higher Level Programming curriculum and focuses on developing and testing classes for representing rectangles and squares. The tasks involve implementing unit tests, handling attributes, serialization, and deserialization, among other Object-Oriented Programming (OOP) concepts in Python.

## Project Structure

The project is organized into the following directories:

- **models:** Contains the main classes (`Base`, `Rectangle`, `Square`) for the project.
- **tests:** Holds unit tests for the classes implemented in the `models` directory.

## Learning Objectives

### General

1. **Unit Testing:**
   - Understand the importance of unit testing.
   - Implement unit tests for classes and methods using the `unittest` module.
   - Validate code using PEP 8 style guidelines.

2. **Serialization and Deserialization:**
   - Learn how to serialize and deserialize a class.
   - Implement methods to convert instances to JSON strings and dictionaries.

3. **Function Arguments:**
   - Understand and utilize `*args` and `**kwargs` in function definitions.
   - Handle named arguments in a function.

### Project Tasks

#### Task 0 - If it's not tested, it doesn't work

Ensure all files, classes, and methods are unit tested and adhere to PEP 8 style guidelines.

#### Task 1 - Base class

Create a base class `Base` with a private class attribute `__nb_objects`, a constructor, and the ability to manage the `id` attribute in derived classes.

#### Task 2 - First Rectangle

Write the `Rectangle` class that inherits from `Base`, with private instance attributes, a constructor, and the ability to manage `id`.

#### Task 3 - Validate attributes

Update the `Rectangle` class to add validation for setter methods and instantiation.

#### Task 4 - Area first

Implement the `area` method in the `Rectangle` class to calculate and return the area of a rectangle.

#### Task 5 - Display #0

Add the `display` method to the `Rectangle` class, which prints the rectangle using the character `#`.

#### Task 6 - \_\_str\_\_

Override the `__str__` method in the `Rectangle` class to provide a custom string representation.

#### Task 7 - Display #1

Improve the `display` method in the `Rectangle` class to consider the `x` and `y` values.

#### Task 8 - Update #0

Add the `update` method to the `Rectangle` class, allowing the modification of attributes with positional arguments.

#### Task 9 - Update #1

Extend the `update` method in the `Rectangle` class to handle keyword arguments.

#### Task 10 - And now, the Square!

Create the `Square` class, inheriting from `Rectangle`, with a constructor that sets width, height, x, y based on the size attribute.

#### Task 11 - Square size

Add a getter and setter for the `size` attribute in the `Square` class.

#### Task 12 - Square update

Implement the `update` method in the `Square` class to allow modification of attributes with positional arguments.

#### Task 13 - Square instance to dictionary representation

Add the `to_dictionary` method to the `Square` class, returning a dictionary representation of the square instance.

#### Task 14 - Dictionary to JSON string

Create a class method in `Base` called `to_json_string` that returns the JSON string representation of a list of dictionaries.

#### Task 15 - JSON string to file

Extend the `Base` class with a class method `save_to_file` that writes the JSON string representation of a list of instances to a file.

#### Task 16 - JSON string to dictionary

Add a static method `from_json_string` to the `Base` class that converts a JSON string to a list of dictionaries.

#### Task 17 - Dictionary to Instance

Introduce the class method `create` in the `Base` class, creating an instance with attributes set from a dictionary.

#### Task 18 - File to instances

Expand the `Base` class with a class method `load_from_file` that returns a list of instances from a file.

## Usage

To run the tests for this project, use the following command:

```bash
python3 -m unittest discover tests
```

You can also run tests for specific modules:

```bash
python3 -m unittest tests/test_models/test_base.py
python3 -m unittest tests/test_models/test_rectangle.py
python3 -m unittest tests/test_models/test_square.py
```
