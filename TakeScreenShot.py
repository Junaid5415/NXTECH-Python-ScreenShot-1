import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
root.title("Junaid Ahmed")
root.geometry('600x400')
mf = tk.Frame(root,width=600,height=400)
mf.pack()
def screenshot():
    myss = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myss.save(save_path+"ss.png")

mybutton = tk.Button(text= "Tap To Capture", command=screenshot,font=10,bg="lightyellow",fg='black')
mybutton.place(x = 230,y=170)

root.mainloop()