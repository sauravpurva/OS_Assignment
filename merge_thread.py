import threading as th

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)/2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

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

        # print "merging", arr

#
# arr = [13,4,1,7,90,24,113,63]
# mergeSort(arr)
