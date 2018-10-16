import random
from Tkinter import *

class Sorting(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.function = {0:self.bubble, 1:self.quick, 2:self.shell}
        self.master.title("Sorting")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S )

        #label for sort intro
        self.label1 = Label(self, text="Select Sort", width=25, height=2)
        self.label1.grid(row=0, column=1, sticky=N)

        #Radio buttons for sorts
        self.v = IntVar()
        for indx, button in enumerate(('Bubble', 'Quick', 'Shell')):
            name = "%s Sort" % button
            button = Radiobutton(self, text=name, variable=self.v, value=indx)
            button.grid(row=1, column=indx, sticky=W+E+N+S)
        button.deselect()

        #button to generate number
        self.button4 = Button(self,text='Generate no.',command=self.gen)
        self.button4.grid(row=2, column=1, sticky=W+E+N+S)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(5, weight=1)

    def create_but2sort(self):
        self.button5 = Button(self, text='start sorting', command=self.sortit)
        self.button5.grid(row=4, column=1, sticky=W+E+N+S)
        self.rowconfigure(5, weight=1 )
        self.columnconfigure(5, weight=1)

    def gen(self):
        self.nums = [random.randint(0, 100) for x in range(10)]
        num = ''.join('%4i' % num for num in self.nums)
        self.label2 = Label(self, text=num, width=2, height=2)
        self.label2.grid(row =3, columnspan=10, sticky = W+E+N+S)
        self.create_but2sort()

    def sortit(self):
        function = self.function[self.v.get()]
        result = function()
        num = ''.join('%4i' % num for num in result)
        self.label3 = Label(self, text=num, width=2, height=2)
        self.label3.grid(row=5, columnspan=10, sticky=W+E+N+S )

    def bubble(self):
        print('bubble to be implemented')
        return sorted(self.nums)

    def shell(self):
        print('shell to be implemented')
        return sorted(self.nums)

    def quick(self):
        print('quick to be implemented')
        return sorted(self.nums)

def main():
    Sorting().mainloop()

if __name__ == "__main__":
    main()