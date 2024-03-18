# Define the path to your desktop
# This path will need to be updated according to the user's OS and username
# Example for Windows: 'C:\\Users\\YourUsername\\Desktop'
# Example for macOS/Linux: '/Users/YourUsername/Desktop'

DESKTOP_PATH = 'C:\Users\YourUsername\Desktop'

# Define organization rules based on file extension
# Keys are file extensions, values are folder names where files will be moved

ORGANIZE_RULES = {
  'txt': 'Text Files',
  'pdf': 'PDF Documents',
  'jpg': 'Images',
  'png': 'Images',
  'docx': 'Word Documents',
  # Add more rules as needed
}

# Log path for recording actions
LOG_PATH = 'logs/cleaner.log'