import Tkinter as tk

# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
# import Tkinter as tk

root = tk.Tk()
item = [2,5,4,1,3]
w = tk.Label(root, text=" ".join(str(item)) )
w.pack()
w1 = tk.Label(root, text=" ".join(str(item)) )
w1.pack()

root.mainloop()
