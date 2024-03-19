import os
import shutil
from datetime import datetime
import logging
import sched
import time
from config import ORGANIZE_RULES, LOG_PATH


scheduler = sched.scheduler(time.time, time.sleep)

logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def organize_desktop(desktop_path):
    """Organize files on the desktop into folders based on file extensions."""
    try:
        files = [f for f in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, f))]
        for file in files:
            try:
                extension = file.split('.')[-1]
                if extension in ORGANIZE_RULES:
                    destination_path = os.path.join(desktop_path, ORGANIZE_RULES[extension])
                    if not os.path.exists(destination_path):
                        os.makedirs(destination_path)
                    shutil.move(os.path.join(desktop_path, file), destination_path)
                    logging.info(f'Moved file {file} to {destination_path}')
                else:
                    logging.info(f'No rule defined for file {file}. Skipping.')
            except Exception as e:
                logging.error(f'Error moving file {file}: {e}')
    except Exception as e:
        logging.error(f'Failed to organize desktop: {e}')

def scheduled_organize(interval, action, actionargs=()):
  """
  Schedules the cleaning action to run at a specified interval.
  
  Parameters:
  - interval (int): The time in seconds between executions of the action.
  - action (callable): The function to be executed at each scheduled interval.
  - actionargs (tuple, optional): Arguments to pass to the action function. Default to an empty tuple.
  """
  
  scheduler.enter(interval, 1, action, actionargs)
  action()
  scheduler.run

if __name__ == "__main__":
  logging.info('Desktop cleaner started.')
  # Example: Schedule the desktop organizing to run every 24 hours (86400 seconds)
  scheduled_organize(86400, organize_desktop)
  logging.info('Desktop cleaner finished.')