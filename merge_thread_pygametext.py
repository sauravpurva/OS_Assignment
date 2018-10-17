from threading import Thread
import threading as th
import time
import thread
import numpy as np

import Tkinter as tk
import pygame, sys
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 0.5
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

pygame.display.set_caption('Merge Sort')

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        displayarray(arr,mid-1)
        t1 = th.Thread(target=mergeSort, args=(lefthalf,))
        t2 = th.Thread(target=mergeSort, args=(righthalf,))

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        i=0
        j=0
        k=0

        # print "lefthalf: ",lefthalf
        # print "righthalf: ",righthalf

        while i<len(lefthalf) and j<len(righthalf):
        #    print lefthalf[i]," ",righthalf[j]
            if lefthalf[i]<righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
                k=k+1
            else:
                arr[k]=righthalf[j]
                j=j+1
                k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
        displayarray(arr,mid)

def displayarray(arr,mid):
    basicfont = pygame.font.SysFont(None, 30)
    image = pygame.Surface((width - width/5,height - height/5))
    rect = image.get_rect()
    rect.top = height/10
    rect.left =  width/10
    width_per_bar = rect.width/len(arr) - 2

    # ele_text = []
    # ele_textrect = []



    l = 0
    mid = len(arr)/2 -1

    const_width = width_per_bar

    for k in range(0,rect.width,width_per_bar + 2):
        bar = pygame.Surface((width_per_bar,arr[l]*10))
        bar_rect = bar.get_rect()



        if(l <= mid):
            bar.fill(blue)
        else:
            bar.fill(green)
        bar_rect.bottom = rect.height
        bar_rect.left = k

        ele_text =  basicfont.render(str(arr[l]), True, red)
        ele_textrect = ele_text.get_rect()
        ele_textrect.centerx = bar_rect.left + const_width/2
        ele_textrect.centery = bar_rect.bottom - 10

        image.blit(bar,bar_rect)
        image.blit(ele_text,ele_textrect)
        l += 1
        if l == len(arr):
            break



    str_text = 'Array size: '+str(len(arr))
    text = basicfont.render(str_text, True, red)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = height/10
    screen.fill(black)
    screen.blit(image,rect)
    screen.blit(text,textrect)
    # for i in range(0,len(arr)):
    #     screen.blit(ele_text[i],ele_textrect[i])
    pygame.display.update()
    clock.tick(FPS)

'''testing below'''
arr = [100,5,1,3,6,16,4,15,9,30,2,13,8,12,16,7]
n=len(arr)
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.KEYUP:
            pass
        if sorted(arr) != arr:
            mergeSort(arr)
        else:
            displayarray(arr,n/2 - 1)
