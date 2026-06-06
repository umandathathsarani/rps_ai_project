# Rock-Paper-Scissors: Adaptive AI Edition

A desktop application that transforms the classic game of Rock-Paper-Scissors into an exploration of machine learning concepts, Object-Oriented Programming (OOP), and local data persistence.

---

# 📖 Project Overview

Unlike standard Rock-Paper-Scissors games that rely on random number generators, this project features a **stateful AI opponent**. The application actively tracks player behavior, learns from their patterns, and adjusts its strategy in real-time to counter the player's most likely next move.

Coupled with a custom-built Graphical User Interface (GUI) and persistent memory storage, this project demonstrates full-stack desktop application development from algorithmic logic to user experience design.

---

# 🧠 Core Features & Architecture

## 1. Markov Chain Predictive Algorithm

The core of the AI is built on a frequency-based Markov Chain model.

### State Tracking

Instead of tracking total moves, the AI maps transitions.

Example:

> "What does the player usually do after they play Rock?"

### Dynamic Countering

Before making a move, the AI:

1. Evaluates the player's previous move
2. Consults its transition matrix
3. Identifies the statistically most probable next move
4. Automatically plays the counter move

---

## 2. Persistent AI Memory (JSON Serialization)

The AI's transition matrix is not wiped when the application closes.

Utilizing Python's built-in `json` and `os` modules, the AI serializes its memory state into a local file:

```bash
ai_memory.json
```

Upon initialization, the AI deserializes this file, allowing it to retain learned player patterns across multiple gaming sessions.

> The more you play, the harder it becomes to beat.

---

## 3. Custom Graphical User Interface (Tkinter)

The application moves away from standard terminal outputs with a fully integrated, class-based GUI.

### Theming

Implements a custom **"Flat 2D Vintage"** aesthetic with:

* Carefully selected hex-code color palettes
* Typography styling
* Smooth button interactions
* Dynamic result updates

### Modal Architecture

The project utilizes:

```python
tk.Toplevel()
```

to generate custom-themed modal result popups that:

* Seize focus
* Prevent interaction with the main window
* Require acknowledgment before continuing

---

## 4. Object-Oriented Design

The codebase is modular and strictly adheres to OOP principles to ensure maintainability and scalability.

### `SimpleAI` Class

Handles:

* Prediction logic
* Transition matrix updates
* JSON file operations

### `ScoreBoard` Class

Handles:

* Win/loss tracking
* Draw statistics
* Score management

### `RPSGame` Class

Handles:

* Tkinter main loop
* UI rendering
* Event handling
* Cross-class communication

---

# 🗂️ Project Structure

```bash
project-folder/
│
├── ai.py              # AI logic, Markov Chain matrix, and JSON handling
├── gui.py             # Tkinter UI setup, event listeners, and main game loop
├── score.py           # Score tracking and game statistics
├── ai_memory.json     # Auto-generated persistent storage file for the AI
├── README.md          # Project documentation
└── LICENSE.md         # Proprietary license information
```

---

# 🚀 How to Run the Game

Follow these step-by-step instructions to get the game running on your local machine.

---

# Part 1: Prerequisites & Dependencies

Before you begin, ensure you have the following installed on your system:

## Python 3.x

Download and install from:

```text
https://www.python.org/
```

> Make sure to check the box **"Add Python to PATH"** during installation.

## Git

Download and install from:

```text
https://git-scm.com/
```

to clone the repository.

---

## Required Libraries

This project is highly optimized and relies entirely on Python's Standard Library to run.

You do **not** need to install any external packages via `pip` to play the game from source code.

The project utilizes:

* `tkinter` → GUI framework
* `json` → AI memory serialization
* `os` → File system operations
* `math` → Internal calculations
* `random` → Randomized fallback decisions

> **Linux Users:**
> If `tkinter` is not installed by default on your distribution, run:

```bash
sudo apt-get install python3-tk
```

---

# Part 2: Cloning the Repository

Open your terminal (Command Prompt / PowerShell) and run the following commands.

## Clone the Repository

```bash
git clone https://github.com/umandathathsarani/rps_ai_project.git
```

## Navigate into the Project Folder

```bash
cd rps_ai_project
```

---

# Part 3: Running the Application

Once inside the project folder, start the game using:

```bash
python gui.py
```

If `python` does not work depending on your system configuration, try:

```bash
python3 gui.py
```

---

# Optional: Building Your Own Executable (.exe)

Compiled executables are excluded from this repository.

If you want to create a standalone desktop application, you can compile it locally using PyInstaller.

---

## Step 1 — Install PyInstaller

```bash
pip install pyinstaller
```

---

## Step 2 — Build the Executable

```bash
pyinstaller --noconsole --onefile gui.py
```

This command:

* Packages the application into a single executable
* Removes the terminal console window
* Creates a standalone `.exe` file

---

## Step 3 — Launch the Game

After the build completes:

1. Open the newly created `dist` folder
2. Double-click:

```bash
gui.exe
```

to launch your standalone game.

---

# 👤 Author

**Mummullage Binuri Umanda Thathsarani**

---

# ⚖️ License

This project is proprietary. All rights reserved.

You may not copy, reproduce, distribute, publish, display, perform, modify, create derivative works, transmit, or exploit any part of this Software without express written permission.

See the `LICENSE.md` file for full details.
