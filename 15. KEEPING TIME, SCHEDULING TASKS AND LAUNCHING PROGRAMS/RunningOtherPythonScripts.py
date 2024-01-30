import subprocess

# Path to the Python script you want to execute
script_path = "./ProjectSuperStopwatch.py"

# Use subprocess to execute the script
try:
    subprocess.run(["python", script_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing {script_path}: {e}")


