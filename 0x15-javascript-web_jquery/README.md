# 0x15. JavaScript - Web jQuery

This project contains a series of JavaScript scripts that utilize jQuery to perform various DOM manipulation tasks.

## Description

The project consists of several tasks, each focusing on different aspects of JavaScript and jQuery usage in web development. Each task has its own requirements and instructions, aiming to reinforce concepts such as selecting HTML elements, modifying styles and content, making AJAX requests, and more.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Chrome (version 57.0)
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be semistandard compliant with the flag --global $: semistandard *.js --global $
- You must use JQuery version 3.x
- You are not allowed to use var
- HTML should not reload for each action: DOM manipulation, update values, fetch data…

## Installation

To run these scripts, you need to have a web browser installed, such as Google Chrome. You also need to include the jQuery library in your HTML file by adding the following line inside the <head> tag:

```html
<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
```

## Usage

Each task has its own set of JavaScript files (.js) and an HTML file for testing. To test a specific task, simply open the corresponding HTML file in your web browser and observe the behavior as described in the task requirements.

## Tasks

### Task 0: No JQuery

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You must use document.querySelector to select the HTML tag
- You can’t use the JQuery API

[Link to task files](./0-script.js)

### Task 1: With JQuery

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./1-script.js)

### Task 2: Click and turn red

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./2-script.js)

### Task 3: Add `.red` class

Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./3-script.js)

### Task 4: Toggle classes

Write a JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

- The <header> element must always have one class: red or green, never both in the same time and never empty.
- If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./4-script.js)

### Task 5: List of elements

Write a JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:

- The new element must be: <li>Item</li>
- The new element must be added to UL.my_list
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./5-script.js)

### Task 6: Change the text

Write a JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header

- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./6-script.js)

### Task 7: Star wars character

Write a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

- The name must be displayed in the HTML tag DIV#character
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./7-script.js)

### Task 8: Star Wars movies

Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

- All movie titles must be list in the HTML tag UL#list_movies
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./8-script.js)

### Task 9: Say Hello!

Write a JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

- The translation of “hello” must be displayed in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./9-script.js)

### Task 10: No jQuery - document loaded

Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):

- You must use document.querySelector to select the HTML tag
- You can’t use the jQuery API
- Note: Your script must be imported from the <head> tag, not at the end of the HTML

[Link to task files](./100-script.js)

### Task 11: List, add, remove

Write a JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

- The new element must be: <li>Item</li>
- The new element must be added to UL.my_list
- When the user clicks on DIV#add_item: a new element is added to the list
- When the user clicks on DIV#remove_item: the last element is removed from the list
- When the user clicks on DIV#clear_list: all elements of the list are removed
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./101-script.js)

### Task 12: Say hello to everybody!

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
- The translation must be fetched when the user clicks on INPUT#btn_translate
- The translation of “Hello” must be displayed in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You

 must use the JQuery API

[Link to task files](./102-script.js)

### Task 13: And press ENTER

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

- You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
- The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
- The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
- The translation of “Hello” must be displayed in the HTML tag DIV#hello
- You can’t use document.querySelector to select the HTML tag
- You must use the JQuery API

[Link to task files](./103-script.js)

## Author

[Lerato Mgwangqa](https://github.com/Ivyratermgwangqa)
```
