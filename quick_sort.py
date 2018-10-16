from threading import Thread
import threading
import time
import thread

def qsort(sets,left,right):

    i = left
    j = right
    print " the array: ", sets
    print " left is ", left
    print " right is", right
    pivot = sets[(left + right)/2]
    print("thread {0} is sorting {1} and pivot is {2}".format(threading.current_thread(), sets[left:right+1], pivot))

    while(i <= j):
         while(pivot > sets[i]):
             i = i+1
         while(pivot < sets[j]):
             j = j-1
         if(i <= j):
             sets[i],sets[j] = sets[j], sets[i]
             i = i + 1
             j = j - 1

    lthread = None
    rthread = None

    print "The array after pivot positioning ", sets

    if (left < j):
        lthread = Thread(target = lambda: qsort(sets,left,j))
        lthread.start()

    if (i < right):
        rthread = Thread(target=lambda: qsort(sets,i,right))
        rthread.start()

    if lthread is not None: lthread.join()
    if rthread is not None: rthread.join()
    return sets


'''testing below'''
ls = [10,5,1,3,6,4,9,2,8,16,7]
res = qsort(ls, 0, len(ls) - 1)
print(res)
