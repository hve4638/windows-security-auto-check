import os
import winreg
import subprocess

"""
PC-06에 대한 조치 함수
type : link
"""
def solve_pc06():
    # Run the specified command
    os.system("start ms-settings:windowsupdate")

"""
PC-07에 대한 조치 함수
type : link
"""    
def solve_pc07():
    # Run the specified command
    os.system("start ms-settings:windowsupdate")    
    
"""
PC-08(한글업데이트)에 대한 조치 함수
type : link
"""
def solve_pc08_A():
    key_path = r"SOFTWARE\WOW6432Node\HNC\Shared\HncUpdate\HncUtils_2020\HancomStudio"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
    value, _ = winreg.QueryValueEx(key, "FilePath")

    hancom_studio_path = value
    subprocess.run([hancom_studio_path], check=True)       

"""
PC-08(어도비 어크로뱃)에 대한 조치 함수
type : link
"""
def solve_pc08_B():
    url = "https://www.adobe.com/devnet-docs/acrobatetk/tools/ReleaseNotesDC/index.html"
    webbrowser.open(url)
