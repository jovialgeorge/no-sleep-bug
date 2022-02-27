# Source code title: No Sleep Bug
# Source code desc: Simple desktop application to avoid sleep
# Source code author: Jovial
# Source code version: v0.1

# Importing required modules
import os
import json
import sys
import tkinter as tk
from tkinter import *
import traceback


# Global variable declaration
METADATA_FILE_PATH = "metadata.json"
ICON_FILE_PATH = "src/bug-solid.ico"


# To read JSON file data
def read_json_file(file_path):
    file_data = None
    try:
        if os.path.exists(file_path):
            with open(file_path) as f:
                file_data = json.load(f)
    except:
        file_data = None
    return file_data

# To execute main program flow and logic
def main():

    # Reading required meta data from JSON file
    metadata = read_json_file(METADATA_FILE_PATH)
    if metadata is None:
        sys.exit()

    # Initializing main GUI window
    main_window = tk.Tk()  
    main_window.geometry(metadata['default_window_geometry'])  
    main_window.title(metadata['app_title'])  
    main_window.iconbitmap(ICON_FILE_PATH)
    main_window.config(background=metadata['background_colour'])

    # Adding widgets to main GUI window
    app_title = tk.Label(main_window, text = metadata['app_title'], font = ('Verdana', 18, 'bold'), bg = metadata['background_colour']).pack(side = TOP, pady = 10)

    activate_button = tk.Button(main_window, text = "Activate", font = ('Verdana', 10), bg = "#43e846")
    activate_button.pack(side = LEFT, padx = 40, pady = 10, ipadx=20)

    deactivate_button = tk.Button(main_window, text = "Deactivate", font = ('Verdana', 10), bg = "#e84343")
    deactivate_button.pack(side = RIGHT, padx = 40, pady = 10, ipadx=20)
  
    # Executing main GIU window
    main_window.mainloop()


# ----- Main program execution -----
if __name__ == "__main__":
    main()