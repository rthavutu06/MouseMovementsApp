from flask import Flask, request
from flask_cors import CORS
import pyautogui
import subprocess
import os
import json
import os
import time
from datetime import datetime


# Load positions from positions.json
positions_path = os.path.join(os.path.dirname(__file__), 'positions.json')
with open(positions_path, 'r') as f:
    positions = json.load(f)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command', '').lower()

    if command == 'refresh':
        pyautogui.hotkey('f5')
        return {'status': 'success', 'message': 'Desktop refreshed!'}

    elif command == 'open notepad':
        subprocess.run(['notepad.exe'])
        return {'status': 'success', 'message': 'Notepad opened!'}

    elif command == 'open downloads':
        with open('positions.json', 'r') as f:
            positions = json.load(f)

        fe_pos = positions['file_explorer']
        dl_pos = positions['downloads']

        # Move to File Explorer icon and single click
        pyautogui.moveTo(fe_pos['x'], fe_pos['y'], duration=0.5)
        pyautogui.click()
        time.sleep(2)  # Give time for File Explorer to open

        # Move to Downloads and double click
        pyautogui.moveTo(dl_pos['x'], dl_pos['y'], duration=0.5)
        pyautogui.doubleClick()

        return {'status': 'success', 'message': 'Downloads folder opened!'}


    elif command == 'create folder':
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        folder_name = "NewFolder_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        folder_path = os.path.join(desktop_path, folder_name)
        os.makedirs(folder_path)
        return {'status': 'success', 'message': f'Folder created: {folder_name}'}

    elif command == 'move mouse':
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=0.5)
        return {'status': 'success', 'message': 'Mouse moved to center of screen!'}

    else:
        return {'status': 'error', 'message': 'Sorry, I cannot perform this action.'}, 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
