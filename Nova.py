import tkinter
import tkinter.scrolledtext
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import filedialog
from tkinter import messagebox

def open_command():
        filename = filedialog.askopenfilename(parent=root,title='Select a file')
        file = open(filename,mode='rb')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            root.title(filename + "Nova")
            file.close()
 
def save_command():
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
         
def exit_command():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
 
def about_command():
    label = messagebox.showinfo("About", "Nova v1.0")
         
 
def new_command():
    data = textPad.get('1.0',END+'-1c')
    if(len(data)>0):
        if messagebox.askokcancel("Quit", "Do you really want to abandon data?") == 0:
            save_command()
    textPad.delete('1.0', END) 


root = tkinter.Tk(className="Nova")
textPad = tkinter.scrolledtext.ScrolledText(root, width=100, height=80)
 
    
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new_command)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About..", command=about_command)

textPad.pack()
root.mainloop()
