# AI-Based Cyberbullying Detection System

This project is a simple AI-based tool that detects potentially harmful or bullying language in user-submitted text. Built using Python and Streamlit, it flags messages containing common bullying words or phrases.

## Features
- Analyzes user-inputted text to detect harmful language.
- Flags messages containing bullying-related keywords.
- Provides a user-friendly interface with Streamlit.

## How to Run the Project

### Prerequisites
1. Make sure you have Python installed. If not, download it from [python.org](https://www.python.org/).
2. Install the required library `streamlit` by running:
   ```bash
   pip install streamlit

Running the Detection Tool
Open the command prompt in the project directory where app.py is located.
Run the following command:
streamlit run app.py

This will launch the detection tool in your default web browser. Type a message in the input box and click "Analyze" to check for bullying language.
Project Structure
app.py: The main file that runs the detection system using Streamlit.
README.md: Documentation file describing the project.
Sample Detection
User Input: "You are so stupid and useless"
Tool Response: "Warning: Potential bullying language detected! Flagged words: stupid, useless"

User Input: "You did a great job"
Tool Response: "No bullying language detected. You're good to go!"
