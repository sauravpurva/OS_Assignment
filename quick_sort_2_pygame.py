from threading import Thread
import threading
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
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)

pygame.display.set_caption('Quick Sort')

arr_itr = []
labels=[]
index=0

def qsort(arr,low,high):

    if low < high:

        i = low - 1
        pivot = arr[high]
        pi = high

        for j in range(low,high):

            if arr[j] <=pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
                displayarray(arr,j,pi)
        arr[i+1],arr[high] = arr[high],arr[i+1]

        pi = i+1
        print("thread {0} is sorting {1} and pivot is {2}".format(threading.current_thread(), arr[low:high+1], pivot))



        lthread = None
        rthread = None

        print "The array after pivot positioning ", arr
        arr_itr.append([arr[low:pi],arr[pi],arr[pi+1:high+1]])
        displayarray(arr,-1,pi)
        lthread = Thread(target = lambda: qsort(arr,low,pi-1))
        lthread.start()

        rthread = Thread(target=lambda: qsort(arr,pi+1,high))
        rthread.start()

        if lthread is not None: lthread.join()
        if rthread is not None: rthread.join()
        return arr

def displayarray_qs(arr, hlt, pi):
    basicfont = pygame.font.SysFont(None, 30)
    image = pygame.Surface((width - width/5,height - height/5))
    rect = image.get_rect()
    rect.top = height/10
    rect.left =  width/10
    width_per_bar = rect.width/len(arr) - 2

    l = 0
    const_width = width_per_bar

    for k in range(0,rect.width,width_per_bar + 2):
        bar = pygame.Surface((width_per_bar,arr[l]*10))
        bar_rect = bar.get_rect()
        if(l == pi):
            bar.fill(green)
        elif(l==hlt and hlt>0):
            bar.fill(yellow)
        else:
            bar.fill(white)
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


    str_text = 'Pivot: '+str(arr[pi])
    text = basicfont.render(str_text, True, red)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = height/10
    screen.fill(black)
    screen.blit(image,rect)
    screen.blit(text,textrect)
    pygame.display.update()
    clock.tick(FPS)

'''testing below'''
ls = [100,5,1,3,6,16,4,15,9,30,2,13,8,12,16,7]
n=len(ls)
pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            pass
        if event.type == pygame.KEYUP:
            pass
        if sorted(ls) != ls:
            res = qsort(ls, 0, len(ls) - 1)
        else:
            displayarray(ls,0,n-1)



print(res)
