import subprocess
import win32api
import win32com.client
program = r"C:\Program Files (x86)\Microsoft\Skype for Desktop\Skype.exe"
subprocess.Popen(program)
shell = win32com.client.Dispatch("WScript.Shell")
win32api.Sleep(5000)
shell.SendKeys("{ENTER}")
win32api.Sleep(6000)
shell.SendKeys("jacknavii10@gmail.com")
shell.SendKeys("{ENTER}")
win32api.Sleep(7000)
shell.SendKeys("naveen@10")
shell.SendKeys("{ENTER}")
