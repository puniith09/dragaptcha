import os
from typing import Dict

def updateFileData(file_path: str, new_data: Dict) -> None:
    with open(file_path, 'w') as file:
        file.write(str(new_data))

def handle_file_update(message: str, file_path: str, new_data: Dict) -> None:
    if message == "file-update":
        updateFileData(file_path, new_data)