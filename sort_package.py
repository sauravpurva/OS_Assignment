from threading import Thread
import threading as th
import time
import thread
import numpy as np

import Queue

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
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)

orange = (255,165,0)
light_blue = (110,255,255)



arr_itr = []
labels=[]
index=0

def oddEvenSort_thread(arr,out_queue):
    # Initially array is unsorted
    isSorted = 0
    n = len(arr)
    displayarray_oe(arr,2)
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayarray_oe(arr,2)
                isSorted = 0

        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                displayarray_oe(arr,2)
                isSorted = 0

    print "hello",arr,"hello\n"



    out_queue.put(arr)


def oddEvenSort(arr):
#    arr = [15,12,70,32,115,24,8,64,16,128,51,52,84,23,96,6,97,3,99,0]
    thr = []
    afterOE = []
    x = len(arr) % 4
    my_queue = Queue.Queue()

    displayarray_oe(arr,2)

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
    arr = afterOE[:]

    if(sorted(arr)== arr):
        print "SORTED."
        sys.exit()
        sorted(arr)


def displayarray_oe(arr,opt):
    basicfont = pygame.font.SysFont(None, 30)
    image = pygame.Surface((width - width/5,height - height/5))
    rect = image.get_rect()
    rect.top = height/10
    rect.left =  width/10
    width_per_bar = rect.width/len(arr) - 2

    l = 0
    mid = len(arr)/2 -1

    const_width = width_per_bar

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
    pygame.display.update()
    clock.tick(FPS)


def qsort(arr,low,high):

    if low < high:

        i = low - 1
        pivot = arr[high]
        pi = high

        for j in range(low,high):

            if arr[j] <=pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
                displayarray_qs(arr,j,pi)
        arr[i+1],arr[high] = arr[high],arr[i+1]

        pi = i+1
    #    print("thread {0} is sorting {1} and pivot is {2}".format(threading.current_thread(), arr[low:high+1], pivot))



        lthread = None
        rthread = None

        print "The array after pivot positioning ", arr
        arr_itr.append([arr[low:pi],arr[pi],arr[pi+1:high+1]])
        displayarray_qs(arr,-1,pi)
        lthread = Thread(target = lambda: qsort(arr,low,pi-1))
        lthread.start()

        rthread = Thread(target=lambda: qsort(arr,pi+1,high))
        rthread.start()

        if lthread is not None: lthread.join()
        if rthread is not None: rthread.join()
        return arr

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        displayarray_ms(arr,mid-1)
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
        displayarray_ms(arr,mid)


def displayarray_ms(arr,mid):
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


ls = []
option = input('Enter option 1.Quick Sort 2.Merge Sort 3. Odd Even Sort:')
print option

if option not in [1,2,3]:
    option = 1
n = input('Enter number of elements: ')
print n
print "Enter the elements: "
for i in range(0,n):
    x = input()
    ls.append(int(x))

print ls
pygame.init()
pygame.display.set_caption('Sort')
while True:
    if option == 1:

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
                displayarray_qs(ls,0,n-1)
    elif option == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
            if sorted(ls) != ls:
                mergeSort(ls)
            else:
                displayarray_ms(ls,n/2 - 1)

    elif option == 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
            if sorted(ls) != ls:
                print "Again."
                oddEvenSort(ls)
            else:
                print "DONE!"
                displayarray_oe(ls, 2)
