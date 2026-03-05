"""
A simple command-line script to periodically click the left mouse button.

Usage:
  python clicker.py                 # Runs with default 10-second interval
  python clicker.py --interval 5    # Runs with a 5-second interval

To quickly quit the script, press Ctrl+C in the terminal where it's running.

Dependencies:
  This script requires `pyautogui` library to function.
  Install it via: `pip install pyautogui`
"""

import time
import argparse
import sys

try:
    import pyautogui
except ImportError:
    print("Error: pyautogui is not installed. Please install it using: pip install pyautogui")
    sys.exit(1)
except KeyError as e:
    # Handle headless environments (like some CI/CD or ssh sessions without X11) gracefully
    if str(e) == "'DISPLAY'":
        print("Warning: Running in a headless environment (no DISPLAY found). PyAutoGUI requires a graphical environment.")
        # Proceeding to allow testing the loop logic, but we won't be able to click
        pyautogui = None
    else:
        raise

def click():
    if pyautogui:
        pyautogui.click()
    else:
        print("[Mock Click] Left mouse button clicked")

def main():
    parser = argparse.ArgumentParser(description="Periodically click the left mouse button.")
    parser.add_argument(
        '-i', '--interval',
        type=float,
        default=10.0,
        help='Interval between clicks in seconds (default: 10.0)'
    )

    args = parser.parse_args()

    print(f"Starting auto-clicker. Clicking every {args.interval} seconds.")
    print("Press Ctrl+C to quit.")

    try:
        while True:
            # We use smaller sleep intervals to make the script more responsive to Ctrl+C
            # rather than sleeping for the entire interval at once.
            sleep_duration = args.interval
            while sleep_duration > 0:
                time.sleep(min(0.5, sleep_duration))
                sleep_duration -= 0.5

            click()
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")
        sys.exit(0)

if __name__ == "__main__":
    main()
