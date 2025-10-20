# 🐍 Day 24 – Snake Game: High Score Update  

This is my twenty-fourth mini project from the **100 Days of Code: Python Bootcamp** by Angela Yu.  

In this update, I revisited my **Snake Game** from Day 20–21 and added a new feature — **persistent high score storage**. Now, the game remembers your highest score even after you close and reopen it!  

---

## 🛠 Tools Used  
- **Python** (`turtle`, `time`)  
- **File Handling** (read/write text files)  
- **Visual Studio Code**  

---

## 💡 What It Does  
- Tracks the **player’s score** during gameplay  
- Stores the **high score** in an external file (`data.txt`)  
- Automatically **loads** the high score each time the game starts  
- **Updates** the stored score only when a new high score is achieved  
- Displays both **current** and **high scores** dynamically on the screen  

---

## 🧠 What I Practiced  
- Reading and writing text files using Python’s `open()` function  
- Implementing **persistent data storage**  
- Refactoring code to integrate file I/O within an OOP project  
- Reinforcing concepts of **encapsulation** and **data management**  

---

## 📁 View the Code  
- **scoreboard.py** — updated to include file read/write logic for high score  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day24-SnakeGameHighScore/Day24-SnakeGameHighScore/scoreboard.py)  

- **main.py** — runs the main game loop and integrates the updated scoreboard  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day24-SnakeGameHighScore/Day24-SnakeGameHighScore/main.py) 

- **snake.py** — defines the `Snake` class and handles movement, direction changes, and growth  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day20%2621-SnakeGame/Day20%2621-SnakeGame/snake.py)  

- **food.py** — defines the `Food` class that randomly generates food for the snake to eat  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day20%2621-SnakeGame/Day20%2621-SnakeGame/food.py)   

---

⭐ **Lesson Learned:** Adding persistent storage takes your projects to the next level — turning temporary programs into *real* applications that remember user data even after closing!
