import tkinter as tk
from tkinter import filedialog
from cleaner import organize_desktop

def open_file_dialog():
  desktop_path = filedialog.askdirectory()
  # Update DESKTOP_PATH in config or store it in a user preferences file
  
def save_preferences():
  # Save updated preferences
  pass

def run_cleaner():
  organize_desktop()
  
app = tk.Tk()
app.title("Desktop Cleaner")

open_folder_btn = tk.Button(app, text="Select Desktop Folder", command=open_file_dialog)
open_folder_btn.pack()

run_cleaner_btn = tk.Button(app, text="Run Cleaner Now", command=run_cleaner)
run_cleaner_btn.pack()

app.mainloop()