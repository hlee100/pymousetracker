import pyautogui
import keyboard
import time
import os

class CursorToolbox():
    def __init__(self):
        self.recorded_actions = []

    def record_click_action(self):
        x, y = pyautogui.position()
        self.recorded_actions.append((x, y))
        print(f"\n[RECORDED CLICK] -> pyautogui.click({x}, {y})")

    def export_generated_code(self, filename="auto_generated_macro.py"):
        if not self.recorded_actions:
            print("\nNo actions recorded. Script generation canceled.")
            return

        try:
            with open(filename, "w") as f:
                f.write("import pyautogui\n")
                f.write("import time\n\n")
                f.write("# Fail-safe: Moving mouse to any corner aborts pyautogui scripts\n")
                f.write("pyautogui.FAILSAFE = True\n\n")
                f.write("print('Starting automated script in 3 seconds... Move mouse to a corner to cancel.')\n")
                f.write("time.sleep(3)\n\n")

                for index, (x, y) in enumerate(self.recorded_actions):
                    f.write(f"# Action {index + 1}\n")
                    f.write(f"pyautogui.click({x}, {y})\n")
                    f.write("time.sleep(1.0)  # Standard delay between actions\n\n")
                
                f.write("print('Automation sequence complete.')\n")
            
            absolute_path = os.path.abspath(filename)
            print(f"\n🚀 Success! Python script generated at:\n{absolute_path}")
            
        except Exception as e:
            print(f"\nError writing the script file: {e}")

    def _clear_keyboard_buffer(self):
        # Helper to ensure keypresses don't leak into the terminal menu
        time.sleep(0.3)  # Short debounce pause
        while keyboard.is_pressed('esc'):
            time.sleep(0.01)

    def mouseAutomationBuilder(self):
        print("=" * 50)
        print("CURSOR TOOLBOX: MOUSE AUTOMATION BUILDER")
        print("=" * 50)
        print("- Hover over an element and press 'Ctrl+Shift+S' to record a click.")
        print("- Press 'Esc' to finish recording")
        print("-" * 50)

        self.recorded_actions = [] # Clear previous session data
        keyboard.add_hotkey('ctrl+shift+s', self.record_click_action)

        while not keyboard.is_pressed('esc'):
            x, y = pyautogui.position()
            position = f'X: {x:4} Y:{y:4} | Recorded Actions: {len(self.recorded_actions)}' 
            print(position, end='', flush=True)
            print(end='\r')
            time.sleep(0.05)

        keyboard.clear_all_hotkeys()
        print('\n\nStopping mouse recorder...')
        
        self.export_generated_code()
        self._clear_keyboard_buffer()

    def mousePositionTracker(self):
        print("=" * 50)
        print("CURSOR TOOLBOX: MOUSE POSITION TRACKER")
        print("=" * 50)
        print("- Press 'Esc' to stop mouse tracking")
        print("-" * 50)

        while not keyboard.is_pressed('esc'):
            x, y = pyautogui.position()
            position = f'X: {x:4} Y:{y:4}' 
            print(position, end='', flush=True)
            print(end='\r')
            time.sleep(0.05)

        print('\n\nStopping mouse tracker...')
        self._clear_keyboard_buffer()

    def mouseColorPicker(self):
        print("=" * 50)
        print("CURSOR TOOLBOX: MOUSE COLOR PICKER")
        print("=" * 50)
        print("- Press 'Space' to save a color layout.")
        print("- Press 'Esc' to stop color tracking")
        print("-" * 50)

        while not keyboard.is_pressed('esc'):
            x, y = pyautogui.position()

            try:
                r, g, b = pyautogui.pixel(x, y)
                hex_color = f"#{r:02X}{g:02X}{b:02X}"
                color_string = f"RGB: ({r:3}, {g:3}, {b:3}) | HEX: {hex_color}"
            except Exception:
                color_string = "RGB: (N/A, N/A, N/A) | HEX: N/A"

            if keyboard.is_pressed('space'):
                print(f"\n[SAVED COLOR] X: {x:4}, Y: {y:4} | {color_string}")
                time.sleep(0.3) # Avoid double logging

            position = f'X: {x:4} Y:{y:4} | {color_string}'
            print(position, end='', flush=True)
            print(end='\r')
            time.sleep(0.05)

        print('\n\nStopping color picker...')
        self._clear_keyboard_buffer()


def main():
    tracker = CursorToolbox()

    while True:
        print("\n" + "=" * 50)
        print("         CURSOR TOOLBOX CLI INTERFACE")
        print("=" * 50)
        print("1. Mouse Automation Builder (Record macro)")
        print("2. Mouse Position Tracker   (Live X/Y coordinates)")
        print("3. Mouse Color Picker       (Live RGB/HEX picker)")
        print("4. Exit")
        print("-" * 50)

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            tracker.mouseAutomationBuilder()
        elif choice == '2':
            tracker.mousePositionTracker()
        elif choice == '3':
            tracker.mouseColorPicker()
        elif choice == '4':
            print("\nExiting Cursor Toolbox. Goodbye!")
            break
        else:
            if choice != "": # Ignore empty inputs caused by trailing keyboard events
                print(f"\n[ERROR] '{choice}' is an invalid choice. Please enter 1, 2, 3, or 4.")
                time.write(1)

if __name__ == "__main__":
    main()