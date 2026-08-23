import tkinter as tk
from datetime import datetime

LOG_FILE = "keylog.txt"


def log_key(event):
    key = event.keysym
    labels = {"space": "[SPACE]", "Return": "[ENTER]", "BackSpace": "[BACKSPACE]", "Tab": "[TAB]"}
    key = labels.get(key, key)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {key}\n")
    status_label.config(text=f"Key logged: {key}")


def clear_log():
    open(LOG_FILE, "w").close()
    status_label.config(text="Log cleared.")


root = tk.Tk()
root.title("Ethical Keylogger Simulator")
root.geometry("600x400")

tk.Label(root, text="Ethical Keylogger Simulator", font=("Arial", 18, "bold")).pack(pady=20)
tk.Label(root, text="Type test data only. Keys are logged only in this application.").pack(pady=10)
text_box = tk.Text(root, height=8, width=60)
text_box.pack(pady=10)
text_box.bind("<KeyPress>", log_key)
status_label = tk.Label(root, text="Waiting for keyboard input...")
status_label.pack(pady=10)
tk.Button(root, text="Clear Log", command=clear_log).pack(pady=10)
root.mainloop()
