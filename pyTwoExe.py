import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import threading

# Global variable for language selection
language = 'en'
icon_path = None

def set_language(lang):
    """Set the language of the interface."""
    global language
    language = lang
    update_texts()

def update_texts():
    """Update the texts based on the selected language."""
    if language == 'tr':
        file_label.config(text="Python Dosyası Seçin:")
        select_file_button.config(text="Gözat")
        icon_label.config(text="Simge seçilmedi.")
        select_icon_button.config(text="Simge Seç")
        additional_hooks_dir_label.config(text="Ekstra Kanca Dizini:")
        runtime_hook_label.config(text="Çalışma Kancası:")
        exclude_module_label.config(text="Hariç Tutulan Modül:")
        info_button.config(text="Bilgi Göster")
        convert_button.config(text="EXE'ye Dönüştür")
        status_label.config(text="Bekleniyor...")
        open_output_dir_button.config(text="Çıktı Dizini Aç")
    else:
        file_label.config(text="Select Python File:")
        select_file_button.config(text="Browse")
        icon_label.config(text="No icon selected.")
        select_icon_button.config(text="Select Icon")
        additional_hooks_dir_label.config(text="Additional Hooks Directory:")
        runtime_hook_label.config(text="Runtime Hook:")
        exclude_module_label.config(text="Exclude Module:")
        info_button.config(text="Show Info")
        convert_button.config(text="Convert to EXE")
        status_label.config(text="Waiting...")
        open_output_dir_button.config(text="Open Output Directory")

def select_file():
    """Open a file dialog to select a Python file."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")]
    )
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def select_icon():
    """Open a file dialog to select an icon file."""
    global icon_path
    icon_path = filedialog.askopenfilename(
        filetypes=[("Icon Files", "*.ico"), ("All Files", "*.*")]
    )
    icon_label.config(text=f"Icon selected: {icon_path}" if icon_path else "No icon selected.")

def update_output(text, color, font_size=10):
    """Update the output area."""
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text)
    output_text.tag_add("color", "1.0", "end")
    output_text.tag_config("color", foreground=color, font=("Arial", font_size))
    output_text.see(tk.END)
    output_text.config(state=tk.DISABLED)

def run_pyinstaller(command, output_dir):
    """Run PyInstaller and notify the user."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    def stream_output(stream, color):
        for line in iter(stream.readline, ''):
            update_output(line, color)
        stream.close()

    threading.Thread(target=stream_output, args=(process.stdout, 'black')).start()
    threading.Thread(target=stream_output, args=(process.stderr, 'red')).start()

    process.wait()
    if process.returncode == 0:
        update_output("Conversion complete.\n", 'green', font_size=8)
        status_label.config(text="Complete.")
        open_output_dir_button.config(state=tk.NORMAL)
        messagebox.showinfo("Success", f"Conversion complete. Output directory: {output_dir}")
    else:
        update_output(f"Error: PyInstaller process failed.\n", 'red', font_size=10)
        status_label.config(text="An error occurred.")
        messagebox.showerror("Error", "An unexpected error occurred during the PyInstaller process.")

def convert_to_exe(file_path):
    """Convert the Python file to an EXE and handle directories."""
    base_dir, base_name = os.path.split(file_path)
    base_name = os.path.splitext(base_name)[0]
    output_dir = os.path.join(base_dir, base_name)
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure PyInstaller command with distpath and workpath options
    command = [
        'pyinstaller',
        '--onefile',
        '--windowed',
        f'--distpath={output_dir}/dist',
        f'--workpath={output_dir}/build',
        f'--specpath={output_dir}/spec'
    ]
    
    if icon_path:
        command.append(f'--icon={icon_path}')
    
    # Add user-defined parameters
    additional_hooks_dir = additional_hooks_dir_var.get().strip()
    if additional_hooks_dir:
        command.append(f'--additional-hooks-dir={additional_hooks_dir}')
        
    runtime_hook = runtime_hook_var.get().strip()
    if runtime_hook:
        command.append(f'--runtime-hook={runtime_hook}')
    
    exclude_module = exclude_module_var.get().strip()
    if exclude_module:
        command.append(f'--exclude-module={exclude_module}')
    
    command.append(file_path)

    def run():
        """Run PyInstaller in a background thread."""
        run_pyinstaller(command, output_dir)
    
    threading.Thread(target=run, daemon=True).start()

def open_output_dir():
    """Open the output directory in File Explorer."""
    file_path = file_entry.get()
    base_dir, base_name = os.path.split(file_path)
    base_name = os.path.splitext(base_name)[0]
    output_dir = os.path.join(base_dir, base_name)
    os.startfile(output_dir)

def show_info():
    """Show information about available parameters based on selected language."""
    if language == 'tr':
        info_message = (
            "Bu araç, Python dosyalarını EXE'ye dönüştürmek için PyInstaller kullanır.\n\n"
            "Kullanılabilir Parametreler:\n"
            "--additional-hooks-dir: Ekstra kanca dosyaları için dizin.\n"
            "--runtime-hook: Çalışma kancası betiği yolu.\n"
            "--exclude-module: Hariç tutulacak modüller.\n\n"
            "Varsayılan olarak, PyInstaller gerekli importları otomatik olarak algılar ve "
            "bazı parametreleri varsayılan değerlerle kullanır. Bu nedenle, bazı parametreler "
            "otomatik olarak yönetilir ve GUI'de gösterilmez.\n\n"
            "Lütfen aracı kullanmadan önce yukarıdaki bilgileri gözden geçirin."
        )
    else:
        info_message = (
            "This tool uses PyInstaller to convert Python files to EXE.\n\n"
            "Available Parameters:\n"
            "--additional-hooks-dir: Directory for additional hook files.\n"
            "--runtime-hook: Path to the runtime hook script.\n"
            "--exclude-module: Names of modules to be excluded.\n\n"
            "By default, PyInstaller automatically detects necessary imports and uses "
            "some parameters with default values. Therefore, some parameters are managed "
            "automatically and are not shown in the GUI.\n\n"
            "Please review the above information before using the tool."
        )
    messagebox.showinfo("Information", info_message)

# Create the Tkinter GUI
root = tk.Tk()
root.title("Python to EXE Converter")

# Set the window size and center it
window_width = 384
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Language buttons
lang_frame = tk.Frame(root)
lang_frame.pack(side=tk.TOP, anchor=tk.W, pady=5, padx=5)

lang_en_button = tk.Button(lang_frame, text="English", command=lambda: set_language('en'))
lang_en_button.pack(side=tk.LEFT)

lang_tr_button = tk.Button(lang_frame, text="Türkçe", command=lambda: set_language('tr'))
lang_tr_button.pack(side=tk.LEFT)

# File selection
file_label = tk.Label(root, text="Select Python File:")
file_label.pack(pady=5)

file_entry = tk.Entry(root, width=60)
file_entry.pack(pady=5)

select_file_button = tk.Button(root, text="Browse", command=select_file)
select_file_button.pack(pady=5)

# Icon selection
icon_label = tk.Label(root, text="No icon selected.")
icon_label.pack(pady=5)

select_icon_button = tk.Button(root, text="Select Icon", command=select_icon)
select_icon_button.pack(pady=5)

# Additional Parameters
additional_hooks_dir_var = tk.StringVar()
additional_hooks_dir_label = tk.Label(root, text="Additional Hooks Directory:")
additional_hooks_dir_label.pack(pady=5)

additional_hooks_dir_entry = tk.Entry(root, textvariable=additional_hooks_dir_var, width=60)
additional_hooks_dir_entry.pack(pady=5)

runtime_hook_var = tk.StringVar()
runtime_hook_label = tk.Label(root, text="Runtime Hook:")
runtime_hook_label.pack(pady=5)

runtime_hook_entry = tk.Entry(root, textvariable=runtime_hook_var, width=60)
runtime_hook_entry.pack(pady=5)

exclude_module_var = tk.StringVar()
exclude_module_label = tk.Label(root, text="Exclude Module:")
exclude_module_label.pack(pady=5)

exclude_module_entry = tk.Entry(root, textvariable=exclude_module_var, width=60)
exclude_module_entry.pack(pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert to EXE", command=lambda: convert_to_exe(file_entry.get()))
convert_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="Waiting...")
status_label.pack(pady=5)

# Open Output Directory Button
open_output_dir_button = tk.Button(root, text="Open Output Directory", command=open_output_dir, state=tk.DISABLED)
open_output_dir_button.pack(pady=5)

# Show Info Button
info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack(pady=5)

# Output Text Area
output_text = tk.Text(root, height=10, width=60, wrap=tk.WORD, state=tk.DISABLED)
output_text.pack(pady=5)

root.mainloop()
