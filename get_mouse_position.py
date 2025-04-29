import pyautogui
import json
import time
import os

positions = {}

print("Move your mouse to File Explorer icon... (5 seconds)")
time.sleep(5)
fe_pos = pyautogui.position()
positions['file_explorer'] = {'x': fe_pos.x, 'y': fe_pos.y}
print(f"Saved File Explorer position: {fe_pos}")

print("Now move your mouse to Downloads folder... (5 seconds)")
time.sleep(5)
dl_pos = pyautogui.position()
positions['downloads'] = {'x': dl_pos.x, 'y': dl_pos.y}
print(f"Saved Downloads position: {dl_pos}")

# Save to JSON
positions_path = os.path.join(os.path.dirname(__file__), 'positions.json')
with open(positions_path, 'w') as f:
    json.dump(positions, f)

print("Positions saved to positions.json")
