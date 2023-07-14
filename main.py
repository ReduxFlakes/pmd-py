import subprocess
import tkinter as tk


def set_profile(power_mode):
    command = ["powerprofilesctl", "set", power_mode]
    subprocess.run(command)


def get_current_profile():
    command = ["powerprofilesctl", "get"]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    current_power_mode = output
    return current_power_mode


def handle_button_click(power_mode):
    set_profile(power_mode)
    current_profile.configure(text="Current Profile: " + get_current_profile())


# Window creation
window = tk.Tk()
window.title("PMD Python")
window.geometry("300x200")

current_profile = tk.Label(window, text="Current profile: " + get_current_profile())
current_profile.pack(pady=10)

# Profile options
power_saving_btn = tk.Button(
    window, text="Power Saver", command=lambda: handle_button_click("power-saver")
)
power_saving_btn.pack(pady=5)

default_btn = tk.Button(
    window, text="Default", command=lambda: handle_button_click("balanced")
)
default_btn.pack(pady=5)

performance_btn = tk.Button(
    window, text="Performance", command=lambda: handle_button_click("performance")
)
performance_btn.pack(pady=5)

# Start
window.mainloop()
