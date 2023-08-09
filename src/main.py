import os
from src.file_reader import readFileData
from src.file_updater import updateFileData
from src.ui_updater import updateUI

class FileData:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

class UIState:
    def __init__(self, file_content, update_button):
        self.file_content = file_content
        self.update_button = update_button

def main():
    file_data = readFileData(os.getcwd())
    updated_file_data = updateFileData(file_data)
    ui_state = UIState(updated_file_data.content, "update-button")
    updateUI(ui_state)

if __name__ == "__main__":
    main()