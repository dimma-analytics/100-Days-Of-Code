# 📌 Day 6 – CLI To-Do List App  

This is my sixth mini project from the **100 Days of Code: Python Bootcamp**.  
I built a simple **Command-Line Interface (CLI)** To-Do List application to practice **functions, lists, conditionals, and loops**.  
The app lets users manage their tasks directly from the terminal — adding, viewing, marking as done, and deleting tasks — with input validation and clean feedback.

---

## 🛠 Tools Used
- Python (`input()`, `print()`, `if/elif/else`, `while`, `for`, `enumerate()`, `.isdigit()`, `.strip()`, `append()`, `pop()`)
- Visual Studio Code

---

## 💡 What It Does
The app gives users 5 menu options:

1. **Add task** – Create a new task stored in a list as a dictionary (`{"title": ..., "done": False}`)  
2. **View tasks** – See all tasks, numbered, with `[ ]` for incomplete and `[x]` for completed  
3. **Mark task as done** – Change a task’s status from incomplete to complete  
4. **Delete task** – Remove a task from the list  
5. **Exit** – Close the program

**Extra features**:
- Validates inputs (e.g., rejects letters where numbers are expected)
- Handles out-of-range task numbers gracefully
- Keeps running until the user chooses to exit

---

## 🧠 What I Learned
- How to structure a Python CLI app using **functions** for each feature  
- How to use a **while loop** for continuous menu display  
- How to store and manage data with **lists of dictionaries**  
- How to perform **input validation** using `.isdigit()` and range checks  
- How to use **enumerate()** to display numbered lists starting at 1  
- The value of reusing functions (e.g., `view_tasks()` inside other features)

---

## 🖼 Preview
**Click here to view how it works**  
_(https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day6-ToDoList/Day6-todo.py%20-%20Visual%20Studio%20Code%202025-08-13%2005-15-18.mp4)_

---

## 📄 View the Code
**[Click here to open](./Day6-todo.py)**

---

## 📚 Helpful Resources
- [enumerate() – Python Docs](https://docs.python.org/3/library/functions.html#enumerate)  
- [if...else – W3Schools](https://www.w3schools.com/python/python_conditions.asp)  
- [while Loops – W3Schools](https://www.w3schools.com/python/python_while_loops.asp)
