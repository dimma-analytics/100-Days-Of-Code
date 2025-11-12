# 🛰️ Day 33 – ISS Overhead Notifier  

This is my thirty-third mini project from the **100 Days of Code: Python Bootcamp** by Angela Yu.  

In this project, I built an **ISS Overhead Notifier** — a program that automatically checks if the **International Space Station (ISS)** is passing above your location and if it’s **nighttime**, then sends you an **email notification** so you can look up and spot it! 🚀  

---

## 🛠 Tools Used  
- **Python** (`requests`, `smtplib`, `datetime`, `time`)  
- **Visual Studio Code**  

---

## 💡 What It Does  
- Fetches the **real-time position** of the ISS using the **Open Notify API**  
- Checks your **current location** (latitude and longitude)  
- Determines whether it’s **dark enough** to see the ISS (by checking sunrise/sunset times from another API)  
- Sends an **email alert** if the ISS is nearby **and** it’s nighttime  
- Runs continuously, checking every 60 seconds  

---

## 🧠 What I Practiced  
- Working with **public APIs** and handling JSON data  
- Automating repetitive tasks with **loops and scheduling**  
- Sending **automated emails** with Python’s `smtplib`  
- Using **datetime** and **time modules** to manage time-based conditions  
- Strengthening problem-solving and logical thinking  

---

## 📁 View the Code  
- **main.py** — main program file for the ISS Overhead Notifier  
  [Click here to view the code](https://github.com/dimma-analytics/100-Days-Of-Code/blob/main/Day33-ISSOverhead/main.py)  

---
