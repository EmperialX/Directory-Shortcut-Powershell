import os
import subprocess


def install_powershell_functions():
    # Create the WindowsPowerShell directory if it doesn't exist
    powershell_directory = os.path.join(os.path.expanduser("~"), 'Documents', 'WindowsPowerShell')
    if not os.path.exists(powershell_directory):
        os.makedirs(powershell_directory)
        print(f"Created directory '{powershell_directory}'")

    # Define the PowerShell code to set the execution policy and install the functions
powershell_code = fr'''
    Start-Process powershell -Verb RunAs -ArgumentList "-Command", "Set-ExecutionPolicy RemoteSigned"
    Write-Host "Please type Y and press Enter to confirm the change of the execution policy. Afterward, close and reopen PowerShell."
    pause > $null

    function shortme ($shortcutName) {{
        $shortcutPath = "$env:USERPROFILE\shortcuts\$shortcutName.txt"
        $currentDirectory = Get-Location
        New-Item -ItemType File -Path $shortcutPath -Value $currentDirectory
        Write-Host "Shortcut '$shortcutName' created. Use 'runme $shortcutName' to change to this directory in future sessions."
    }}

    function runme ($shortcutName) {{
        $shortcutPath = "$env:USERPROFILE\shortcuts\$shortcutName.txt"
        $shortcutDirectory = Get-Content $shortcutPath
        Set-Location $shortcutDirectory
    }}

    Add-Content $PROFILE "`nfunction shortme {{ param(`$shortcutName) `$shortcutPath = `"$env:USERPROFILE\shortcuts\\`$shortcutName.txt`"; `$currentDirectory = Get-Location; New-Item -ItemType File -Path `$shortcutPath -Value `$currentDirectory; Write-Host `"`nShortcut '$shortcutName' created. Use 'runme `$shortcutName' to change to this directory in future sessions.`" }}" 
    Add-Content $PROFILE "`nfunction runme {{ param(`$shortcutName) `$shortcutPath = `"$env:USERPROFILE\shortcuts\\`$shortcutName.txt`"; `$shortcutDirectory = Get-Content `$shortcutPath; Set-Location `$shortcutDirectory }}" 

    . $PROFILE

'''
# Define the help page
help_page = f"\n{'*' * 10} QuickDir {'*' * 10}\n\n"
help_page += "QuickDir is a PowerShell script that allows you to create shortcuts to frequently used directories and change to those directories quickly.\n\n"
help_page += "To create a shortcut, use the 'shortme' command followed by the name of the shortcut you want to create. For example:\n\n"
help_page += "    shortme myshortcut\n\n"
help_page += "This will create a shortcut named 'myshortcut' that points to the current directory.\n\n"
help_page += "To change to a directory using a shortcut, use the 'runme' command followed by the name of the shortcut. For example:\n\n"
help_page += "    runme myshortcut\n\n"
help_page += "This will change to the directory associated with the 'myshortcut' shortcut.\n\n"

# Display the help page
print(help_page)


# Use the subprocess module to run the PowerShell code
process = subprocess.Popen(['powershell.exe', '-Command', powershell_code], stdout=subprocess.PIPE)
output, error = process.communicate()

# Print the output and error messages
if output:
    print(output.decode('utf-8'))
if error:
    print(error.decode('utf-8'))


# Call the function to install the PowerShell functions
install_powershell_functions()
