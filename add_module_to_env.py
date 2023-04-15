import os

# Ask the user for the directory containing the quickdir PowerShell module
module_path = input("Please enter the directory containing the quickdir PowerShell module (e.g. C:\\Users\\ASUS\\shortcuts\\powershell-directory-shortcuts): ")

# Ask for confirmation before proceeding
confirm = input(f"Are you sure you want to add {module_path} to the system environment variables? (y/n): ")
if confirm.lower() != "y":
    print("Aborting...")
    exit()

# Get the current system environment variables
system_vars = os.environ["Path"].split(";")

# Check if the module path is already in the system variables
if module_path in system_vars:
    print("The module path is already in the system environment variables.")
else:
    # Check if the directory exists
    if not os.path.exists(module_path):
        print(f"The directory {module_path} does not exist. Aborting...")
        exit()
    
    # Add the module path to the system variables
    system_vars.append(module_path)

    # Set the new system environment variables
    os.environ["Path"] = ";".join(system_vars)

    print("The module path has been added to the system environment variables.")

# Display a message to remind the user to restart their command prompt or terminal
print("Please restart your command prompt or terminal for the changes to take effect.")
