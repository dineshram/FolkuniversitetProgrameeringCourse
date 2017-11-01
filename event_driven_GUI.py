# Use from X import * to save having to preface everything 
# as tkinter.xxx
from Tkinter import *

# Create the application class which defines the GUI 
# and the event handling methods
class KeysApp(Frame):
    def __init__(self): # use constructor to build GUI
        Frame.__init__(self)
        self.txtBox = Text(self)
        self.txtBox.bind("<space>", self.doQuitEvent)
        self.txtBox.pack()
        self.pack()

    def doQuitEvent(self,event):
        import sys
        sys.exit()
        

# Now create an instance and start the event loop running
myApp = KeysApp()
myApp.mainloop()


