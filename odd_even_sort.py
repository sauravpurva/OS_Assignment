import threading as th
import merge_thread as mt



def oddEvenSort(arr):
    # Initially array is unsorted
    isSorted = 0
    n = len(arr)
    while isSorted == 0:
        isSorted = 1
        temp = 0
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0

    print "hello",arr,"hello\n"
    return arr



arr = [15,12,70,32,115,24,8,64,16,128,51,52,84,23,96,6,97,3,99,0]
thr = []
afterOE = []
x=0
thr.append(th.Thread(target=oddEvenSort,args=(arr[0:4],)) )
thr.append(th.Thread(target=oddEvenSort,args=(arr[4:8],)) )
thr.append(th.Thread(target=oddEvenSort,args=(arr[8:12],)) )
thr.append(th.Thread(target=oddEvenSort,args=(arr[12:16],)) )
thr.append(th.Thread(target=oddEvenSort,args=(arr[16:20],)) )

for thread in thr:
    thread.start()
    x=x+1

print "no of threads", x


for thread in thr:
    ret = thread.join()
    print ret,"\n"

print afterOE, " is the combined array\n"

print "after threads",arr
mt.mergeSort(arr)

print "after mergesort", arr
