# Clicker Script

## Description
This Python script allows you to perform repeated left-clicks at a specified position on your screen using Python's `pyautogui` and Windows API (`win32api`).

## Requirements
- Python 3.x
- `pyautogui` library
- `pywin32` (also known as `win32api`)

## Installation
1. Make sure Python 3.x is installed on your system.
2. Install the required libraries:

## Usage
1. Run the script.
2. Position your mouse cursor where you want the clicks to occur.
3. Press the right mouse button (`RBUTTON`) to trigger the script.
4. The script will simulate two left-clicks at the current cursor position, repeated every 0.1 seconds.

## Customization
- You can modify the number of clicks by adjusting the `clicks` parameter in the `click` function.
- To change the click interval, adjust the `time.sleep()` value.

## Important Notes
- Ensure that the script is used responsibly and in accordance with local laws and regulations.
- The script is designed for Windows systems and may not work on other operating systems.
