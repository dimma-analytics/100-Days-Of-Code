# 🐍 Day 23 – The Turtle Crossing Game  

This is my twenty-third mini project from the **100 Days of Code: Python Bootcamp** by Angela Yu.  

In this project, I built the **Turtle Crossing Game**, inspired by the classic arcade game *Frogger*. The player controls a turtle trying to cross a busy road filled with moving cars — the goal is to reach the other side safely without getting hit!  

---

## 🛠 Tools Used  
- **Python** (`turtle`, `time`, `random`)  
- **Visual Studio Code**  

---

## 💡 What It Does  
- Lets the player control a turtle that moves upward with each key press  
- Continuously generates moving cars at random intervals and speeds  
- Detects **collisions** between the player and cars — game ends if hit  
- Increases **difficulty** (car speed) each time the player successfully crosses the road  
- Displays the player’s **current level** on a scoreboard that updates dynamically  

---

## 🧠 What I Practiced  
- Breaking a project into multiple classes for better structure (`Player`, `CarManager`, `Scoreboard`)  
- Implementing **collision detection** between the player and cars  
- Using the **OOP approach** to manage player movement, car creation, and game logic  
- Controlling **game speed and difficulty scaling** using loops and delays  
- Managing **screen updates and refresh rates** for smooth animation  

---

## 👀 Preview  
![Turtle Crossing Game Screenshot](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day23-TurtleCrossingGame/Day23.png)  

---

## 📁 View the Code  
- **player.py** — defines the `Player` class and controls turtle movement  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day23-TurtleCrossingGame/Day23-turtle-crossing-start/player.py)  

- **car_manager.py** — defines the `CarManager` class, handles car generation and movement  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day23-TurtleCrossingGame/Day23-turtle-crossing-start/car_manager.py)  

- **scoreboard.py** — defines the `Scoreboard` class that tracks and displays the level  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day23-TurtleCrossingGame/Day23-turtle-crossing-start/scoreboard.py)  

- **main.py** — the main game file that brings everything together and runs the game loop  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day23-TurtleCrossingGame/Day23-turtle-crossing-start/main.py)  

---

⭐ **Lesson Learned:** Structuring a game using OOP makes your code more modular, organized, and scalable — a big step toward real-world Python development!
