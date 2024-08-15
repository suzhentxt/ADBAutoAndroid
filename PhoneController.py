import subprocess

a = str(subprocess.check_output("adb devices", shell=True))
a = a.replace("b'List of devices attached\\r\\n", "")
a = a.replace("\\tdevice\\r", "")
a = a.replace("\\n", "")

print(a[:-2])