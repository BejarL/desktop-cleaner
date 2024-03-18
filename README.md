# Desktop Cleaner Script

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Scheduling](#scheduling)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)


## Overview
The Desktop Cleaner Script is a Python application designed to help users automatically organize
files on their desktop into specified folders based on file extensions or predefined rules. 
This tool aims to keep your desktop neat and make file management easier.

## Features
* Automatic File Organization: Moves files into folders based on their extensions.
* Scheduled Cleaning: Option to set the script to run automatically at specified intervals (e.g., daily
or weekly).
* Customizable Rules: Users can define their own rules for how files should be organized.
* Simple GUI: A basic graphical user interface for easier configuration and manual triggering of the
cleaning process.

## Requirements
* Python 3.6 or newer
* Operating System: Windows, macOS, or Linux

## Installation
1. Clone the repository or download the ZIP file.
  git clone https://github.com/BejarL/desktop-cleaner.git
2. Navigate to the project directory.
  cd desktop-cleaner
3. (Optional) Create a virtual environment and activate it.
  python -m venv venv
  source venv/bin/activate # On Windows use `venv\Scripts\activate`
4. Install any dependencies.
  pip install -r requirements.txt

## Configuration
Before running the script, you need to configure your rules ans settings in `config.py`. Edit the 
`DESKTOP_PATH` to point to your desktop directory and define `ORGANIZE_RULES` for how you want your files 
organized.
  
Example config.py:
    `DESKTOP_PATH = '/Users/username/Desktop'  # Update this path
    ORGANIZE_RULES = {
        'txt': 'Text Files',
        'pdf': 'PDF Documents',
        ...
    }`
## Usage
* To run the desktop cleaner:
    python cleaner.py
* For GUI.py
    python gui.py

## Scheduling
To enable scheduled cleaning, refer to the `scheduled_organize` function in `cleaner.py`. By default,
it's ser to run every 24 hours. Adjust the interval as needed.

## Troubleshooting
* Script doesn't run: Ensure Python is correctly installed and that you're using the right version.
* Files aren't moved: Check that `DESKTOP_PATH` in `config.py` correctly point to your desktop.
  Ensure file permissions allow the script to move files.

## Contributing
Contributions are welcome! If you have suggestions for improvement or bugs fixes, please open an issue
or submit a pull request.