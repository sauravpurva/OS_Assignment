from threading import Thread
import threading as th
import time
import thread
import numpy as np

import Tkinter as tk
import pygame
from pygame.locals import *

scr_size = (width,height) = (900,600)
FPS = 0.5
screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
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
    image = pygame.Surface((width - width/5,height - height/5))
    rect = image.get_rect()
    rect.top = height/10
    rect.left =  width/10
    width_per_bar = rect.width/len(arr) - 2

    l = 0
    mid = len(arr)/2 -1
    for k in range(0,rect.width,width_per_bar + 2):
        bar = pygame.Surface((width_per_bar,arr[l]*10))
        bar_rect = bar.get_rect()
        if(l <= mid):
            bar.fill(blue)
        else:
            bar.fill(green)
        bar_rect.bottom = rect.height
        bar_rect.left = k

        image.blit(bar,bar_rect)
        l += 1
        if l == len(arr):
            break


    screen.fill(black)
    screen.blit(image,rect)
    pygame.display.update()
    clock.tick(FPS)

'''testing below'''
arr = [100,5,1,3,6,16,4,15,9,30,2,13,8,12,16,7]
n=len(arr)
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
