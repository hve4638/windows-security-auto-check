import subprocess
import winreg
import re, os
import ctypes
user32 = ctypes.WinDLL('user32')

'''
PC10에 대한 조치 함수
    # link
'''
def solve_pc10():
    try:
        subprocess.run("wscui.cpl", shell=True, check=True)
    except subprocess.CalledProcessError:
        user32.MessageBoxW(None, '관리 창을 띄울 수 없습니다', 'Error!', 0)



'''
PC11에 대한 조치 함수
    # solve (관리자 권한 필요)
'''
def solve_pc11(): # PC11 방화벽
    reg_handle = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    
    # path of registry
    registry_path = r'SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\StandardProfile'
    key = winreg.OpenKey(reg_handle, registry_path, 0, winreg.KEY_WRITE)
    # name of specific value
    value_name = 'EnableFirewall'
    
    winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 0x00000001)


"""
PC12에 대한 조치 함수
type : solve
"""
def solve_pc12(): # PC12 화면 보호기
    reg_handle = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    
    # path of registry
    registry_path = r'Control Panel\Desktop'
    key = winreg.OpenKey(reg_handle, registry_path, 0, winreg.KEY_WRITE)
    # name of specific value
    value_name = 'ScreenSaveActive'
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, '1')
    
    # path of registry
    registry_path = r'Control Panel\Desktop'
    key = winreg.OpenKey(reg_handle, registry_path, 0, winreg.KEY_WRITE)
    # name of specific value
    value_name = 'ScreenSaverIsSecure'
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, '1')
    
    # path of registry
    registry_path = r'Control Panel\Desktop'
    key = winreg.OpenKey(reg_handle, registry_path, 0, winreg.KEY_WRITE)
    # name of specific value
    value_name = 'ScreenSaveTimeout'
    winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, '600')
    
"""
PC13에 대한 조치 함수 
type : solve (관리자 권한 필요)
"""
def solve_pc13(): # PC13 이동식 미디어 차단
    reg_handle = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    
    # path of registry
    registry_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer'
    key = winreg.OpenKey(reg_handle, registry_path, 0, winreg.KEY_WRITE)
    # name of specific value
    value_name = 'NoDriveTypeAutoRun'
    
    winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 0x000000ff)
    
"""
PC19에 대한 조치 함수 
type : solve (관리자 권한 필요)
"""
def solve_pc19(): # PC19 외부 연결 차단
    reg_handle = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

    # path of registry
    registry_path = r'SYSTEM\CurrentControlSet\Control\Remote Assistance'
    key = winreg.OpenKey(reg_handle, registry_path, 0, winreg.KEY_WRITE)
    # name of specific value
    value_name = 'fAllowToGetHelp'
    
    winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, 0x00000000)



