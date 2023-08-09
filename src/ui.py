```python
import os
from src.ui_updater import updateUI

class UIState:
    def __init__(self, file_content, update_button):
        self.file_content = file_content
        self.update_button = update_button

def initialize_ui():
    ui_state = UIState("", False)
    return ui_state

def handle_ui_update(ui_state, message):
    if message == "ui-update":
        ui_state = updateUI(ui_state)
    return ui_state

def main():
    ui_state = initialize_ui()
    while True:
        message = os.read()
        ui_state = handle_ui_update(ui_state, message)

if __name__ == "__main__":
    main()
```