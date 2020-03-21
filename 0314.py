# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 13:53:05 2020

@author: TAITRA
"""

import pygame
BLACK =( 0, 0, 0)
WHITE =(255,255,255)
pygame.init()
meme =(255,255, 0)
size=(700,500)
screen=pygame.display.set_mode(size)
pygame.display.set_caption("ddddddddddddd")
done=False
clock=pygame.time.Clock
while not done:
    if event.type==pygame.QUIT:
        done=True
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
   