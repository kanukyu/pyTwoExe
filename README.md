# Python to EXE Converter a.k.a pyTwoExe

This tool allows you to convert Python scripts into standalone executables using **PyInstaller**. It provides a graphical interface where you can select your Python file, specify an icon for the executable, and customize parameters such as hooks, runtime hooks, and excluded modules. The interface is available in both English and Turkish.

## Screenshots

### English GUI
![pyTwoExe GUI EN](https://cdn.discordapp.com/attachments/1260029917396205700/1283541374167421010/pyTwoExeGUI_EN.png?ex=66e35e8e&is=66e20d0e&hm=2740c96141f4721d99b55692db53d0cc7a7f60495c57dffe2076a1fa54c7847a&)

### English Info Popup
![pyTwoExe INFO EN](https://cdn.discordapp.com/attachments/1260029917396205700/1283541374880190484/pyTwoExeINFO_EN.png?ex=66e35e8e&is=66e20d0e&hm=769e66d010c26087ebe59b4713e8a0961a0455f6372bcef93a78aa8b3079ad76&)

### Turkish GUI
![pyTwoExe GUI TR](https://cdn.discordapp.com/attachments/1260029917396205700/1283541374578331668/pyTwoExeGUI_TR.png?ex=66e35e8e&is=66e20d0e&hm=2e5df0735ac2e2549b9e976725353d79a24eac6bebb4b7e8715e1fa12efea909&)

### Turkish Info Popup
![pyTwoExe INFO TR](https://cdn.discordapp.com/attachments/1260029917396205700/1283541373869363260/pyTwoExeINFO_TR.png?ex=66e35e8e&is=66e20d0e&hm=314017b94078affeb08c25bb2063bf6b3a675562305989b07a2ab7163383a5ca&)

## Requirements

Ensure you have the following installed:
- [**Python 3.12+**](https://www.python.org/downloads/)
- [**PyInstaller**](https://pypi.org/project/pyinstaller/) (Install via `pip install pyinstaller`)

> **Note**: If you don't have Python and pip installed, you can use [this PowerShell script](https://github.com/kanukyu/pythonPipInstaller) to automatically install them.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kanukyu/pyTwoExe.git
   ```
2. Navigate to the project folder:
   ```bash
   cd pyTwoExe
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute script:
   ```bash
   python pyTwoExe.py
   ```
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
     python pyTwoExe.py
     ```

2. **PowerShell**:
   - Open PowerShell (`Win + X`, select **Windows PowerShell**).
   - Navigate to the project folder:
     ```bash
     cd path\to\your\project
     ```
   - Run the script:
     ```bash
     python pyTwoExe.py
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
     python pyTwoExe.py
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

This project is licensed under the Apache-2.0 License.
