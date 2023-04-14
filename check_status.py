#!/usr/bin/env python
import os

# Get the path to the PowerShell profile file
profile_path = os.path.expanduser("~\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1")

# Check if the file exists and is not empty
if os.path.exists(profile_path) and os.path.getsize(profile_path) > 0:
    # Open the file and read its contents
    with open(profile_path, "r") as profile_file:
        profile_content = profile_file.read()

    # Check if the functions are defined in the file
    if "function shortme" in profile_content and "function runme" in profile_content:
        print("The feature is installed.")
    else:
        print("The feature is not installed.")
else:
    print("The PowerShell profile file does not exist or is empty.")
