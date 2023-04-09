import ctypes
import os
a=os.getcwd()
ctypes.windll.user32.SystemParametersInfoW(20,0,'C:\\Windows\\lp.png',0)
