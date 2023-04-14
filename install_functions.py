#!/usr/bin/env python
import os
import subprocess

def install_powershell_functions():
    # Define the PowerShell code to install the functions
    powershell_code = r'''
    function shortme ($shortcutName) {
        $shortcutPath = "$env:USERPROFILE\shortcuts\$shortcutName.txt"
        $currentDirectory = Get-Location
        New-Item -ItemType File -Path $shortcutPath -Value $currentDirectory
        Write-Host "Shortcut '$shortcutName' created. Use 'runme $shortcutName' to change to this directory in future sessions."
    }

    function runme ($shortcutName) {
        $shortcutPath = "$env:USERPROFILE\shortcuts\$shortcutName.txt"
        $shortcutDirectory = Get-Content $shortcutPath
        Set-Location $shortcutDirectory
    }

    Add-Content $PROFILE "`nfunction shortme { param(`$shortcutName) `$shortcutPath = `"$env:USERPROFILE\shortcuts\\`$shortcutName.txt`"; `$currentDirectory = Get-Location; New-Item -ItemType File -Path `$shortcutPath -Value `$currentDirectory; Write-Host `"`nShortcut '$shortcutName' created. Use 'runme `$shortcutName' to change to this directory in future sessions.`" }"
    Add-Content $PROFILE "`nfunction runme { param(`$shortcutName) `$shortcutPath = `"$env:USERPROFILE\shortcuts\\`$shortcutName.txt`"; `$shortcutDirectory = Get-Content `$shortcutPath; Set-Location `$shortcutDirectory }" 

    . $PROFILE
    '''

    # Use the subprocess module to run the PowerShell code
    process = subprocess.Popen(['powershell.exe', '-Command', powershell_code], stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output and error messages
    if output:
        print(output.decode('utf-8'))
    if error:
        print(error.decode('utf-8'))

    # Define the help page
    help_page = r'''
    ***********************************************************************
    *                                                                     *
    *                                                                     *
    *                             QuickDir                                *
    *                       PowerShell Functions                         *
    *                                                                     *
    *                                                                     *
    ***********************************************************************

    DESCRIPTION:
        QuickDir is a set of PowerShell functions that allows you to create and
        manage shortcuts to frequently used directories.

    FUNCTIONS:
        - shortme
            Creates a new shortcut to the current directory.

        - runme
            Changes to the directory specified by the given shortcut.

    USAGE:
        To create a new shortcut, use the following command:
            shortme shortcutName

        To change to a directory specified by a shortcut, use the following command:
            runme shortcutName

    EXAMPLES:
        To create a shortcut called 'work' for the current directory, use the following command:
            PS C:\Users\JohnDoe> shortme work

        To change to the directory specified by the 'work' shortcut, use the following command:
            PS C:\Users\JohnDoe> runme work

    For more information, visit https://github.com/yourusername/quickdir
    '''

    # Print the help page
    print(help_page)

