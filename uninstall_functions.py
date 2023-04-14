#!/usr/bin/env python
import os

# Define a function to remove the shortcut files
def remove_shortcut(shortcut_name):
    shortcut_path = os.path.expanduser(f"~/shortcuts/{shortcut_name}.txt")
    os.remove(shortcut_path)
    print(f"Shortcut '{shortcut_name}' removed.")

# Define a function to remove the PowerShell functions from the profile
def remove_shortme_runme():
    profile_path = os.path.expanduser("~/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1")
    with open(profile_path, "r") as f:
        lines = f.readlines()
    new_lines = [l for l in lines if "shortme" not in l and "runme" not in l]
    with open(profile_path, "w") as f:
        f.writelines(new_lines)
    print("PowerShell functions removed from the profile.")

# Remove the functions and shortcut files
remove_shortcut("MyShortcut")
remove_shortme_runme()

# Print a thank you message
print("Thank you!")

