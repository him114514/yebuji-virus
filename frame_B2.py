import pyautogui as ui
import random
ui.FAILSAFE = False
class shubiao:
    def move(self,a,b):
        ui.moveTo(random.randint(a,b), random.randint(a,b),duration=0)
S=shubiao()        
while True:
    S.move(0,1000)
