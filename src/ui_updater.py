```python
import os
from src.file_reader import FileData
from src.ui import UIState

def updateUI(file_data: FileData, ui_state: UIState, file_content_id: str, update_button_id: str):
    # Update the UI state based on the updated file data
    ui_state.content = file_data.content
    ui_state.updated = True

    # Update the DOM element with id "file-content" to display the updated file content
    os.system(f"document.getElementById('{file_content_id}').innerHTML = '{file_data.content}'")

    # Enable the update button
    os.system(f"document.getElementById('{update_button_id}').disabled = false")

def handleFileUpdate(message: str, file_data: FileData, ui_state: UIState):
    if message == "file-update":
        # Update the UI after a file update
        updateUI(file_data, ui_state, "file-content", "update-button")

def handleUIUpdate(message: str, ui_state: UIState):
    if message == "ui-update" and ui_state.updated:
        # Reset the UI state after an update
        ui_state.updated = False
        ui_state.content = ""
```
