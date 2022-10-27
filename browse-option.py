# Source : https://www.youtube.com/watch?v=q8WDvrjPt0M&ab_channel=BroCode

from tkinter import * 
from tkinter import filedialog

def openFile():
  filepath = filedialog.askopenfilename(initialdir='D:\\04_Personal_Stuff\\Cooking', 
                                       title= "Open file okay?")
  file = open(filepath,'r' )
  print(file.read())
  file.close()

window = Tk()
button = Button(text = "Open", command=openFile)
button.pack()
window.mainloop()