def hello_world(arr):
    for each in arr:
        each = each +2
    return arr


arr1 = [4,7,8,90]
ret = hello_world(arr1)
print ret, " is after func"
