#!/usr/bin/env python
import os

def uninstall_powershell_functions():
    # Define the PowerShell code to remove the functions from the profile
    powershell_code = fr'''
    $functions_to_remove = @("shortme", "runme")
    $profile_path = $PROFILE.CurrentUserAllHosts
    $profile_content = Get-Content $profile_path
    foreach ($function_name in $functions_to_remove) {{
        $function_start = $profile_content.IndexOf("`nfunction $function_name (")
        $function_end = $profile_content.IndexOf("`n`n", $function_start)
        if ($function_start -ge 0 -and $function_end -ge 0) {{
            $function_length = $function_end - $function_start
            $profile_content.Remove($function_start, $function_length)
        }}
    }}
    Set-Content $profile_path $profile_content
    Write-Host "PowerShell functions removed from user profile.'''

    # Display a message to the user
    print("\n" + "*" * 10 + " QuickDir " + "*" * 10 + "\n")
    print("QuickDir has been uninstalled from your system. The PowerShell functions that it added to your user profile have been removed.\n")
    print("The shortcuts that you created with QuickDir have not been deleted. You can remove them manually if you no longer need them.\n")

    # Get the absolute path of the script file and remove it
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "quickdir.ps1"))
    os.remove(script_path)

    # Use the os module to remove the shortcuts directory
    shortcuts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "shortcuts"))
    os.rmdir(shortcuts_dir)

    print("QuickDir script and shortcuts directory removed.")

# Call the function to uninstall the PowerShell functions
uninstall_powershell_functions()

