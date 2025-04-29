# MouseMovementsApp

A lightweight local automation tool that mimics the Windows "Run" dialog. This app accepts simple text commands and performs mouse-based actions like opening folders or refreshing the desktop.

## ✨ Features

- Mimics Windows "Run" popup appearance
- Executes commands via actual mouse movements
- Opens apps or folders like Downloads/File Explorer
- Extensible and modular backend using Flask and PyAutoGUI
- Frontend built with React

## 🛠 Tech Stack

- **Frontend**: React
- **Backend**: Python (Flask)
- **Automation**: PyAutoGUI
- **Window Automation**: AutoHotKey v2.0

## 📁 Project Structure

MouseMovementsApp/ ├── app.py # Flask backend ├── frontend/ # React frontend ├── launch_react_window.ahk # AutoHotKey script to open the React app ├── get_mouse_position.py # Utility to fetch screen coordinates ├── positions.json # Stored mouse positions for each command ├── venv/ # Python virtual environment


## 🚀 Setup & Run Locally

### 1. Backend

cd MouseMovementsApp
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

2. Frontend
bash
Copy code
cd frontend
npm install
npm start

3. Launch UI with AutoHotKey
Double-click launch_react_window.ahk or press Ctrl + E (hotkey) to open the UI.

🔧 Add New Commands
Use get_mouse_position.py to capture coordinates.

Add entries to positions.json with the new command and coordinates.

Restart the backend.

💡 Future Improvements
Add voice input support
Support for drag and keyboard actions
System tray integration