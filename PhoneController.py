import subprocess

a = str(subprocess.check_output("adb devices", shell=True)).replace("b'List of devices attached\\r\\n", "").replace("\\tdevice\\r", "").split("\\n")

print(a[:-2])