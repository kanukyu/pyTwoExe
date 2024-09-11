# Python to EXE Converter a.k.a pyTwoExe

This tool allows you to convert Python scripts into standalone executables using **PyInstaller**. It provides a graphical interface where you can select your Python file, specify an icon for the executable, and customize parameters such as hooks, runtime hooks, and excluded modules. The interface is available in both English and Turkish.

## Requirements

Ensure you have the following installed:
- [**Python 3.12+**](https://www.python.org/downloads/)
- [**PyInstaller**](https://pypi.org/project/pyinstaller/) (Install via `pip install pyinstaller`)

> **Note**: If you don't have Python and pip installed, you can use [this PowerShell script](https://github.com/kanukyu/pythonPipInstaller) to automatically install them.

## How to Use

### Running the Tool in Different Terminals

1. **Command Prompt (CMD)**:
   - Open CMD (`Win + R`, type `cmd`, press `Enter`).
   - Navigate to the project folder:
     ```bash
     cd path\to\your\project
     ```
   - Run the Python script:
     ```bash
     python your_script.py
     ```

2. **PowerShell**:
   - Open PowerShell (`Win + X`, select **Windows PowerShell**).
   - Navigate to the project folder:
     ```bash
     cd path\to\your\project
     ```
   - Run the script:
     ```bash
     python your_script.py
     ```
   - If you encounter an execution policy error, use the following command:
     ```bash
     Set-ExecutionPolicy RemoteSigned
     ```

3. **Git Bash**:
   - Open Git Bash.
   - Navigate to the project folder:
     ```bash
     cd /path/to/your/project
     ```
   - Run the Python script:
     ```bash
     python your_script.py
     ```

## Features

- **Convert Python Files to EXE**: Convert `.py` files into `.exe` using PyInstaller.
- **Custom Icon**: Select a custom `.ico` file to be used as the icon for the executable.
- **Additional Parameters**: Specify additional hooks, runtime hooks, and exclude specific modules during the conversion process.
- **Multilingual Interface**: Supports English and Turkish languages.

## Troubleshooting

If Python or PyInstaller is not recognized, ensure that:
- Python is installed and added to your system's `PATH`.
- PyInstaller is installed via `pip install pyinstaller`.

## License

This project is licensed under the MIT License.
