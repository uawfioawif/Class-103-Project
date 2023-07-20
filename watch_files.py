import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/nicho/OneDrive/Desktop/Coding Class/Projects/Python/Class 103 Project/files'

class FileEventHandler(FileSystemEventHandler):
  def on_created(self, event):
    print(event.src_path, "has been created")
  def on_deleted(self, event):
    print(event.src_path, "has been deleted")
  def on_moved(self, event):
    print(event.src_path, "has been moved")
  def on_modified(self, event):
    print(event.src_path, "has been modified")

eventHandler = FileEventHandler()
observer = Observer()

observer.schedule(eventHandler, from_dir, recursive=True)
observer.start()
try:
  while True:
    time.sleep(2)
    print('Running...')
except KeyboardInterrupt:
  observer.stop()
  print('Stopped!')