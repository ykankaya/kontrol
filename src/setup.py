import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"include_files": ["alarm.wav"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Kontrol",
        version = "1.0",
        description = "Kontrol application for ASSC graduation project",
        options = {"build_exe": build_exe_options},
        executables = [Executable("kontrol.py",
                                  shortcutName="Kontrol",
                                  shortcutDir="DesktopFolder",
                                  base=base,
                                  icon="icon.ico")])

