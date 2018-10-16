
from threading import Thread
import threading as th

import Queue

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

orange = (255,165,0)
light_blue = (110,255,255)

pygame.display.set_caption('Odd Even Sort')


def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        displayarray(arr,1)
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

        displayarray(arr,1)

def oddEvenSort_thread(arr,out_queue):
    # Initially array is unsorted
    isSorted = 0
    n = len(arr)
    displayarray(arr,2)
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayarray(arr,2)
                isSorted = 0

        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayarray(arr,2)
                isSorted = 0

    print "hello",arr,"hello\n"

    out_queue.put(arr)


def oddEvenSort(arr):
#    arr = [15,12,70,32,115,24,8,64,16,128,51,52,84,23,96,6,97,3,99,0]
    thr = []
    afterOE = []
    x = len(arr) % 4
    my_queue = Queue.Queue()

    displayarray(arr,2)

    i=0
    while( i< len(arr) ):
        print "i is ",i
        thr.append(th.Thread(target=oddEvenSort_thread, args=(arr[i:i+4], my_queue, )))
        i = i+4

    # thr.append(th.Thread(target=oddEvenSort,args=(arr[0:4],my_queue,)) )
    # thr.append(th.Thread(target=oddEvenSort,args=(arr[4:8],my_queue,)) )
    # thr.append(th.Thread(target=oddEvenSort,args=(arr[8:12],my_queue,)) )
    # thr.append(th.Thread(target=oddEvenSort,args=(arr[12:16],my_queue,)) )
    # thr.append(th.Thread(target=oddEvenSort,args=(arr[16:20],my_queue,)) )

    for thread in thr:
        thread.start()
        x=x+1

    for thread in thr:
        ret = thread.join()

    while(my_queue.empty() == False ):
        afterOE.extend(my_queue.get())
    print "afterOE is ", afterOE

    mergeSort(afterOE)

    print "after mergesort", afterOE


def displayarray(arr,opt):
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
        if(opt==1):
            if(l <= mid):
                bar.fill(blue)
            else:
                bar.fill(green)
        if(opt==2):
            if(l % 2 ==0):
                bar.fill(light_blue)
            else:
                bar.fill(orange)
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
            oddEvenSort(arr)
        else:
            print "DONE!"
            displayarray(arr, 2)
