# 🏓 Day 22 – The Pong Game  

This is my twenty-second mini project from the **100 Days of Code: Python Bootcamp**.  

I recreated the classic **Pong Game** using Python’s `turtle` graphics module — a two-player arcade game where players control paddles to bounce a ball back and forth. The goal is simple: don’t miss the ball!  

---

## 🛠 Tools Used  
- **Python** (`turtle`, `time`)  
- **Visual Studio Code**  

---

## 💡 What It Does  
- Simulates a classic Pong game with **two paddles** and a **ball**  
- Allows **two players** to control paddles using keyboard keys (`W/S` for the left paddle and `Up/Down` arrows for the right paddle)  
- Detects **collisions** between the ball, paddles, and screen walls  
- Updates the **scoreboard** whenever a player misses the ball  
- Resets the ball position and continues gameplay automatically after each point  

---

## 🧠 What I Practiced  
- Structuring a multi-class project with separate files for paddles, ball, and scoreboard  
- Applying **Object-Oriented Programming (OOP)** concepts like inheritance and encapsulation  
- Implementing **collision detection** logic and real-time updates  
- Handling **keyboard events** for smooth paddle movement  
- Managing game loops and animation timing using the `time` module  

---

## 👀 Preview  
![Pong Game Screenshot](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day22-PongGame/Day22.png)  

---

## 📁 View the Code  
- **paddle.py** — defines the `Paddle` class and handles paddle creation and movement  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day22-PongGame/Day22-PongGame/paddle.py)  

- **ball.py** — defines the `Ball` class, handles movement, bouncing, and resetting after a point  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day22-PongGame/Day22-PongGame/ball.py)  

- **scoreboard.py** — defines the `Scoreboard` class that tracks and displays each player’s score  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day22-PongGame/Day22-PongGame/scoreboard.py)  

- **main.py** — the main game file that ties everything together and runs the game loop  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day22-PongGame/Day22-PongGame/main.py)  
