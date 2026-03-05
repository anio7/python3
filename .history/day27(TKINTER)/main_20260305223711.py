import tkinter

FONT = ("Arial",24,"bold")

#initialize an object to the tkinter class with its title and minsize
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 500)

#create a label
label = tkinter.Label(text = "I am a label",font = FONT)
#calls the label and pack it to the screen with its default being 
label.pack(side = "left")
























#leave at the end of the program
window.mainloop()

