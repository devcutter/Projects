#gui module
from Tkinter import *

#create the window
root = Tk()

#window setting
root.title("Chat Interface")
root.geometry("600x50")

app = Frame(root)
app.grid()
button1 = Button(app, text = "start")
button1.grid()



#kick off the event loop
root.mainloop()

