import threading as th
import merge_thread as mt
import Queue

def oddEvenSort(arr,out_queue):
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
    out_queue.put(arr)


arr = [15,12,70,32,115,24,8,64,16,128,51,52,84,23,96,6,97,3,99,0]
thr = []
afterOE = []
x = len(arr) % 4
my_queue = Queue.Queue()

i=0
while( i< len(arr) ):
    print "i is ",i
    thr.append(th.Thread(target=oddEvenSort, args=(arr[i:i+4], my_queue, )))
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

mt.mergeSort(afterOE)

print "after mergesort", afterOE
