```markdown
# JavaScript Warm-Up

This repository contains solutions for JavaScript warm-up tasks.

## Environment Setup

1. Install Node.js (version 14.x):

    ```bash
    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

2. Install `semistandard`:

    ```bash
    sudo npm install semistandard --global
    ```

## Task Instructions

### Task 0: First constant, first print

- Create a constant variable called `myVar` with the value "JavaScript is amazing".
- Use `console.log(...)` to print the value.

### Task 1: 3 languages

- Print three lines: "C is fun", "Python is cool", and "JavaScript is amazing".

### Task 2: Arguments

- Print a message based on the number of arguments passed:
  - If no arguments: "No argument".
  - If one argument: "Argument found".
  - Otherwise: "Arguments found".

### Task 3: Value of my argument

- Print the first argument passed to the script. If no arguments, print "No argument".

### Task 4: Create a sentence

- Print two arguments in the format: "{arg1} is {arg2}".

### Task 5: An Integer

- Print "My number: {first argument}" if the first argument can be converted to an integer.

### Task 6: Loop to languages

- Print three lines using an array of strings and a loop.

### Task 7: I love C

- Print "C is fun" x times, where x is the first argument.

### Task 8: Square

- Print a square using the character "X". The size is the first argument.

### Task 9: Add

- Write a function `add(a, b)` that returns the addition of two integers.

### Task 10: Factorial

- Write a script that computes and prints a factorial.

### Task 11: Second biggest!

- Print the second biggest integer from the list of arguments.

### Task 12: Object

- Update the script to replace the value 12 with 89 in the object.

### Task 13: Add file

- Write a function that returns the addition of two integers.

### Task 14: Const or not const

- Update a script to replace the value of `myVar` with 333.

### Task 15: Call me Moby

- Write a function that executes a given function x times.

### Task 16: Add me maybe

- Write a function that increments and calls a function.

### Task 17: Increment object

- Update a script by adding a new function `incr` that increments the integer value.

## Running the Scripts

Each script is an individual JavaScript file. You can run them using Node.js:

```bash
node filename.js
```

Make sure the scripts are executable:

```bash
chmod +x filename.js
```

## Checking Code Style

Ensure your code follows the semistandard style:

```bash
semistandard filename.js
```

---

Happy coding!
```

This `README.md` provides an overview of the tasks, environment setup, instructions for running scripts, and checking code style. You can modify it as needed for your specific requirements.
