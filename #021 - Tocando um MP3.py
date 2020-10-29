"""Faça um programa que abra e reproduza o áudio de um arquivo mp3"""

'''Primeiramente é necessário copiar o arquivo e colar junto na lista de exerícios e eles devem ter o mesmo nome'''

import pygame
pygame.init() #Essa bibilioteca em espocífio, é preciso incializar
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
