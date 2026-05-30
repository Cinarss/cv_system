from datetime import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        message = f"[{timestamp}] {func.__name__} called"
        print("[LOG]", message)

        with open("log.txt", "a") as f:
            f.write(message + "\n")

        return func(*args, **kwargs)
    return wrapper