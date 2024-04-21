from datetime import datetime

def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def getCurrentMinute():
    return datetime.now().strftime("%M")