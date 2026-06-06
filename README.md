# Rock-Paper-Scissors AI

A standalone desktop application featuring a machine learning-inspired opponent that adapts to player behavior using a Markov Chain prediction algorithm.

## Features
* **Adaptive AI (Markov Chain):** The AI tracks state transitions based on player history to predict and counter future moves.
* **Persistent Memory:** Game states and AI memory are serialized and stored via JSON, allowing the AI to "learn" across multiple sessions.
* **Graphical User Interface (GUI):** A custom-themed, flat 2D vintage UI built natively with Tkinter, featuring modal popups for round results.
* **Session Score Tracking:** Live tracking of player wins, AI wins, and ties.
* **Standalone Executable:** Fully packaged into a zero-dependency `.exe` file for Windows using PyInstaller.

## Technologies Used
* **Python 3** (Core Logic & AI)
* **Tkinter** (Graphical Interface)
* **PyInstaller** (Application Packaging)
* **JSON** (Data Persistence)

## How to Run
### Option 1: Run the Executable (Windows Only)
1. Navigate to the `dist/` directory.
2. Double-click `gui.exe` to launch the game.

### Option 2: Run from Source
1. Ensure Python 3.x is installed on your machine.
2. Clone the repository.
3. Run the main interface script:
   ```bash
   python gui.py