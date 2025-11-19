# 🧠 Day 34 – Quizzler App (API Trivia Quiz)

This is my thirty-fourth mini project from the **100 Days of Code: Python Bootcamp**.

In this project, I built a **Quiz App** that pulls real True/False trivia questions from an **online API** and displays them in a clean graphical interface using `tkinter`.

---

## 🛠 Tools Used
- **Python** (`tkinter`, `requests`)
- **API Integration** (Open Trivia Database API)
- **Object-Oriented Programming**
- **Visual Studio Code**

---

## 💡 What It Does
- Fetches **10 random True/False questions** from a real API
- Converts API data into custom `Question` objects
- Displays questions one at a time in a GUI
- Lets the user choose **True** or **False**
- Shows **green/red feedback** based on the answer
- Tracks and updates the **score** as the quiz progresses
- Ends the quiz with a final score message

---

## 🧠 What I Practiced
- Understanding **APIs**, endpoints, and parameters
- Sending GET requests using the `requests` module
- Parsing **JSON** responses
- Creating and connecting multiple Python classes
- Building interactive GUI layouts with `tkinter`
- Managing quiz flow, scoring, and user feedback

---

## 📁 View the Code
- **data.py** — fetches the questions from the trivia API
[Click here to view the code][https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day34-QuizzlerApp/Day34-QuizzlerAapp/data.py)
- **main.py** — ties all components together
[Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day34-QuizzlerApp/Day34-QuizzlerAapp/main.py)
- **question_model.py** — defines the `Question` blueprint
[Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day34-QuizzlerApp/Day34-QuizzlerAapp/question_model.py)
- **quiz_brain.py** — handles quiz logic and scoring
[Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day34-QuizzlerApp/Day34-QuizzlerAapp/quiz_brain.py)
- **ui.py** — builds the user interface
[Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day34-QuizzlerApp/Day34-QuizzlerAapp/ui.py)
- **images** — contains the button images
[Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/tree/main/Day34-QuizzlerApp/Day34-QuizzlerAapp/images)

---

⭐ **Lesson Learned:** APIs + OOP + GUI = A perfect combo for building fun, interactive, real-world apps!
