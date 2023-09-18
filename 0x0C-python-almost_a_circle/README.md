# Python Rectangle Class

This README provides an overview of the Python Rectangle class and its usage. The code snippets provided are part of an assignment involving the implementation of a Rectangle class.

## Table of Contents

- [Introduction](#introduction)
- [Files and Directory Structure](#files-and-directory-structure)
- [Class Base](#class-base)
- [Class Rectangle](#class-rectangle)
- [Validating Attributes](#validating-attributes)
- [Calculating Area](#calculating-area)
- [Displaying the Rectangle](#displaying-the-rectangle)
- [String Representation](#string-representation)
- [Updating Object Attributes](#updating-object-attributes)

## Introduction

The Python code provided in this repository demonstrates the implementation of a Rectangle class. The class is designed to manage rectangle objects with attributes such as width, height, x-coordinate, y-coordinate, and a unique identifier.

## Files and Directory Structure

- `models/`: This directory contains Python modules for the Rectangle class and its base class.
  - `base.py`: Defines the base class `Base` for managing object IDs.
  - `rectangle.py`: Defines the `Rectangle` class, which inherits from `Base` and represents rectangles.

- `tests/`: This directory contains unit tests for the Rectangle class.

## Class Base

The `Base` class, defined in `models/base.py`, is responsible for managing object IDs. It has a private class attribute `__nb_objects` for counting the number of objects created. The constructor `__init__` handles the assignment of object IDs.

## Class Rectangle

The `Rectangle` class, defined in `models/rectangle.py`, represents rectangles with attributes:
- `__width` (width of the rectangle)
- `__height` (height of the rectangle)
- `__x` (x-coordinate of the rectangle)
- `__y` (y-coordinate of the rectangle)

The class constructor `__init__` initializes these attributes, and it inherits the ID management from the `Base` class. Getter and setter methods are provided for each attribute, and validation checks are performed to ensure that attributes meet the required criteria.

## Validating Attributes

Attributes such as width, height, x, and y are validated as follows:
- If an attribute is not an integer, a `TypeError` is raised.
- If width or height is less than or equal to 0, a `ValueError` is raised.
- If x or y is less than 0, a `ValueError` is raised.

## Calculating Area

The `Rectangle` class includes a method `area` that calculates and returns the area of the rectangle.

## Displaying the Rectangle

The `display` method is provided to display the rectangle using the '#' character. It takes into account the x and y coordinates.

## String Representation

The `__str__` method is overridden to provide a string representation of the `Rectangle` object in the format `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.

## Updating Object Attributes

The `update` method allows for updating object attributes by providing arguments in a specific order:
1. Object ID
2. Width
3. Height
4. x-coordinate
5. y-coordinate

## Running Tests

The provided tests in the `tests/` directory can be run using the following command:

```
python3 -m unittest discover tests
```

The tests cover various aspects of the `Rectangle` and `Base` classes, including attribute validation and method functionality.

Feel free to refer to the individual code files for more details, and modify or extend the code as needed for your specific requirements.
