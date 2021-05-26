###### Tocando uma música MP# ######



import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()