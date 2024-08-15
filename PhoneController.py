import subprocess

print(subprocess.check_output("adb devices", shell=True))