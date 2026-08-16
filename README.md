🎯 Number Guessing Game Using Python

A simple and interactive Number Guessing Game developed using Python and Tkinter. This project provides a graphical user interface where the player has to guess a randomly generated number between 1 and 100.

The game includes three difficulty levels — Easy, Medium, and Hard — with different numbers of attempts available to the player. The player receives helpful feedback after each guess, such as "Too low!" or "Too high!", making the game interactive and engaging.

✨ Features
🎯 Random number generation between 1 and 100
🎮 Three difficulty levels:
Easy — 10 attempts
Medium — 7 attempts
Hard — 5 attempts
📊 Score tracking starting from 100 points
🔢 User input validation
⚠️ Warning messages for invalid inputs
💡 Feedback after every incorrect guess
❤️ Attempts-left tracking
🎉 Success message when the correct number is guessed
❌ Game-over message when all attempts are used
🔄 New Game functionality
🖥️ User-friendly graphical interface using Tkinter
🎨 Simple and clean GUI design
🛠️ Technologies Used
Python
Tkinter — for creating the graphical user interface
Random module — for generating the secret number
🎮 How the Game Works

When the game starts, a random number between 1 and 100 is generated. The player first selects a difficulty level and clicks Start Game. Based on the selected difficulty, the player receives a fixed number of attempts.

For every guess, the program checks whether the entered value is valid and within the range of 1 to 100. If the guess is smaller than the secret number, the player receives a "Too low!" message. If the guess is greater, the game displays "Too high!". The number of remaining attempts and the score are updated after each valid guess.

If the player correctly guesses the number, a success message displays the final score. If all available attempts are exhausted, the game displays the correct number and ends the current round.

📂 Project Structure
Number-Guessing-Game/
│
└── Number Guessing Game Using Python.py
📚 Learning Outcomes

This project demonstrates practical use of Python programming, object-oriented programming, GUI development, event handling, conditional statements, loops, exception handling, random number generation, and user input validation.

It is a beginner-friendly project suitable for learning how Python can be used to create interactive desktop applications.

🚀 Future Improvements

Possible improvements include adding sound effects, difficulty-based number ranges, a high-score system, a timer, multiple rounds, player names, improved GUI styling, and storing scores for future sessions.

👨‍💻 Project Purpose

The main purpose of this project is to build a simple yet interactive Python application while practicing Tkinter GUI development and core Python programming concepts.
