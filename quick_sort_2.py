from threading import Thread
import threading
import time
import thread

def qsort(arr,low,high):

    if low < high:

        i = low - 1
        pivot = arr[high]

        for j in range(low,high):

            if arr[j] <=pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]

        pi = i+1
        print("thread {0} is sorting {1} and pivot is {2}".format(threading.current_thread(), arr[low:high+1], pivot))
        lthread = None
        rthread = None

        print "The array after pivot positioning ", arr
        lthread = Thread(target = lambda: qsort(arr,low,pi-1))
        lthread.start()

        rthread = Thread(target=lambda: qsort(arr,pi+1,high))
        rthread.start()

        if lthread is not None: lthread.join()
        if rthread is not None: rthread.join()
        return arr


'''testing below'''
ls = [10,5,1,3,6,4,9,2,8,16,7]
res = qsort(ls, 0, len(ls) - 1)
print(res)
