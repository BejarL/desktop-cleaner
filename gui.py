import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import cleaner
import threading
import time

class DesktopCleanerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Desktop Cleaner")
        self.master.geometry("500x250")  # Adjusted for additional elements
        self.master.resizable(True, True)

        self.master.option_add("*Font", "Helvetica 12")
        self.master.tk_setPalette(background="#f0f0f0", foreground="black",
                                  activeBackground="#e0e0e0", activeForeground="black")

        self.create_widgets()
        self.schedule_thread = None
        self.scheduling_active = False

    def create_widgets(self):
        self.instructions = tk.Label(self.master, text="Select your desktop folder, run the cleaner, or schedule automatic cleaning.",
                                     wraplength=480, justify="left")
        self.instructions.pack(pady=10)

        self.open_folder_btn = tk.Button(self.master, text="Select Desktop Folder", command=self.open_file_dialog)
        self.open_folder_btn.pack(pady=5)

        self.run_cleaner_btn = tk.Button(self.master, text="Run Cleaner Now", command=self.run_cleaner)
        self.run_cleaner_btn.pack(pady=5)

        self.schedule_btn = tk.Button(self.master, text="Schedule Automatic Cleaning", command=self.schedule_cleaning)
        self.schedule_btn.pack(pady=5)

        self.status_label = tk.Label(self.master, text="", wraplength=480)
        self.status_label.pack(pady=10)

    def open_file_dialog(self):
        desktop_path = filedialog.askdirectory()
        if desktop_path:
            self.desktop_path = desktop_path
            self.status_label.config(text=f"Selected Path: {desktop_path}")
        else:
            self.status_label.config(text="No path selected. Please select a path.")

    def run_cleaner(self):
        if hasattr(self, 'desktop_path'):
            cleaner.organize_desktop(self.desktop_path)
            messagebox.showinfo("Operation Completed", "Desktop cleaned successfully.")
        else:
            messagebox.showwarning("No Path Selected", "Please select a path first.")

    def schedule_cleaning(self):
        if not hasattr(self, 'desktop_path'):
            messagebox.showwarning("No Path Selected", "Please select a path first.")
            return

        interval = simpledialog.askinteger("Input", "Enter the cleaning interval in seconds:",
                                           parent=self.master, minvalue=10, maxvalue=86400)
        if interval:
            if self.schedule_thread and self.scheduling_active:
                self.scheduling_active = False
                self.schedule_thread.join()

            self.scheduling_active = True
            self.schedule_thread = threading.Thread(target=self.run_scheduled_cleaning, args=(interval,))
            self.schedule_thread.start()
            self.status_label.config(text=f"Scheduled cleaning every {interval} seconds.")

    def run_scheduled_cleaning(self, interval):
        while self.scheduling_active:
            time.sleep(interval)
            if self.scheduling_active:  # Check again to avoid running after stopping
                cleaner.organize_desktop(self.desktop_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = DesktopCleanerGUI(root)
    root.mainloop()