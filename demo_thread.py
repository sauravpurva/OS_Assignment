import threading as th

def sum(a,b):
    for i in range(0,5):
        print a+b," "

def multiply(a,b):
    for i in range(0,5):
        print a*b, " "

t1 = th.Thread(target=sum, args=(10,5,));
t2 = th.Thread(target=multiply, args=(10,5,));

t1.start()
t2.start()

t1.join()
t2.join()

print "Done"
print "Hope no errors :D"
