from threading import Thread
import threading
import time
import thread

import Tkinter as tk

arr_itr = []
labels=[]
index=0

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
        arr_itr.append([arr[low:pi],arr[pi],arr[pi+1:high+1]])
        lthread = Thread(target = lambda: qsort(arr,low,pi-1))
        lthread.start()

        rthread = Thread(target=lambda: qsort(arr,pi+1,high))
        rthread.start()

        if lthread is not None: lthread.join()
        if rthread is not None: rthread.join()
        return arr


'''testing below'''
ls = [10,5,1,3,6,4,15,9,2,13,8,12,16,7]
n=len(ls)
root = tk.Tk()
res = qsort(ls, 0, len(ls) - 1)

for each in arr_itr:
    print " --> ",each[0],each[1],each[2], " "
    labels.append( tk.Label(root, text=" ".join( str(each[0]) ) ) )
    labels.append(tk.Label(root, text = "Pivot is: "+str(each[1])) )
    labels.append(tk.Label(root, text =" ".join(str(each[2]))) )

i=0
while(i<len(labels)-1):

    labels[i].grid(row=i,column=0)
    labels[i+1].grid(row=i,column=2)
    labels[i+2].grid(row=i,column=4)
    i=i+3

root.mainloop()
print(res)
