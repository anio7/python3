import tkinter

FONT = ("Arial")
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width = 500, height = 500)

#create a label
label = tkinter.Label(text = "I am a label")
#calls the label and pack it to the screen
label.pack()
























#leave at the end of the program
window.mainloop()

