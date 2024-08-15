import subprocess

a = str(subprocess.check_output("adb devices", shell=True))

print(a.replace("b'List of devices attached\\r\\n", ""))