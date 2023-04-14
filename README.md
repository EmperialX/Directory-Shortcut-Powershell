# QuickDir-Powershell
"Shortcuts Powershell" is a Python command-line tool that allows users to create and manage custom directory shortcuts. It simplifies navigation by allowing users to change to frequently-used directories with a single command for future session.
This project provides a set of PowerShell functions that allow you to create and manage directory shortcuts in your PowerShell sessions.

## Installation
### Prerequisites


Before you can use this project, you need to have the following software installed on your computer:
```
Windows PowerShell or PowerShell Core
Python 3.x

```


### Installation Steps

To install the PowerShell directory shortcuts, follow these steps:

Download or clone this repository to your local machine.
```
git clone https://github.com/EmperialX/QuickDir-Powershell.git

```

Open a command prompt or PowerShell window.
```
powershell

```

Navigate to the directory where you saved the repository.
```
cd QuickDir-Powershell

```

### Install
Run the following command to install the PowerShell functions:
```
python install_functions.py

```
This will create two PowerShell functions named shortme and runme that you can use to create and manage directory shortcuts.



## Usage

### Creating Shortcuts

To create a shortcut to the current directory, run the following command:
```
shortme MyShortcut

```

This will create a file named MyShortcut.txt in the `%USERPROFILE%\shortcuts` directory that contains the full path to the current directory.
Running Shortcuts


To change to a directory that has a shortcut, run the following command:
```
runme MyShortcut

```


This will change your current directory to the directory that is stored in the `MyShortcut.txt` file.

##  Checking the Installation Status

To check whether the PowerShell functions are installed, run the following command:
```
python check_status.py

```


This will check the PowerShell profile file to see if the shortme and runme functions are defined. If they are defined, it will print "The feature is installed." Otherwise, it will print "The feature is not installed."


## Uninstalling the PowerShell Functions

To uninstall the PowerShell functions and remove all the shortcut files, run the following command:

python uninstall_functions.py

This will remove the `shortme` and `runme` functions from the PowerShell profile file and delete all the shortcut files.
## Contributing

If you find a bug or have a feature request, please open an issue on the GitHub repository. Pull requests are also welcome.
## License

This project is licensed under the MIT License. See the LICENSE file for details.
## Directory Structure

Here is the directory structure of this project:
```
powershell-directory-shortcuts/
├── README.md
├── check_status.py
├── install_functions.py
├── uninstall_functions.py
├── LICENSE
└── shortcuts/
    ├── MyShortcut.txt
    ├── AnotherShortcut.txt
    └── ...

```


The `check_status.py`, `install_functions.py`, and `uninstall_functions.py` files are Python scripts that are used to check the installation status, install the PowerShell functions, and uninstall the PowerShell functions, respectively.

The shortcuts directory is where the shortcut files are stored. When you create a new shortcut, a new text file with the shortcut name is created in this directory.
Contact

If you have any questions or concerns, please contact me at [github](https://github.com/EmperialX).
