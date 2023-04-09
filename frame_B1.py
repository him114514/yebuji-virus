import pygame
import sys
pygame.init()
pygame.display.set_caption("yebuji")
screen = pygame.display.set_mode([621, 500])
screen.fill([255, 255, 205])
img = pygame.image.load("C:\\Windows\\jiji.bmp")
screen.blit(img, [0, 0])
pygame.display.flip()
pygame.mixer.init()
pygame.mixer.music.load('C:\\Windows\\精神病拉面.MP3')
pygame.mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pass
