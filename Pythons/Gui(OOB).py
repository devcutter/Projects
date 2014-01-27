# class with Tkinter
from ChatServer import *
from Tkinter import *

class Application(Frame):
    """ A GUI application with three buttons """

    def __init__(self, master):
        """initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create 3 buttons that do nothing"""
        #create first button
        self.button1 = Button(self, text = "Start")
        self.button1.bind
        self.button1.grid()

    def onclick(self):
        

#create new window
root = Tk()
root.title("Chat")
root.geometry("200x85")

app = Application(root)

root.mainloop()
