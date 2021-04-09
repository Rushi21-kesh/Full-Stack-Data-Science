#import libraries 
import os
import win32api
from tkinter import *
import tkinter as tk

#create a object of Tk
guiapk = Tk()
guiapk.title("File system")
guiapk.iconbitmap("icon.ico")
#guiapk.geometry("1500x1000")
guiapk.config(bg='lightsteelblue')

path_var = tk.StringVar()
#ext_var = tk.StringVar()

# function
def spec_path():

    path = path_var.get()
    #ext = ext_var.get()
    ext = clicked.get()
    drive = drived.get()
    
    #check path is given or not
    if len(path)>0:
        dp = path
    else:
        dp = drive
    #change directory according to requirement
    os.chdir(dp)
    path = os.path.dirname(os.path.realpath(dp))
    for root, dirs, files in os.walk(dp):
        for file in files:
            if file.endswith('.' + ext):
                output.insert(END,root + '/' + str(file)+'\n')
    path_var.set("")
   # ext_var.set("")

def refresh():
    output.delete('1.0',END)


# create drop down manu for extention
ext_options = ['exe','docx','pdf','json',"txt","ppt","yml"]
clicked = StringVar()
clicked.set("Extention : ")
drop = OptionMenu(guiapk,clicked,*ext_options)
drop.config(bg='lightsteelblue',font='lato 10 bold')

# create drop down manu for drive
drv = win32api.GetLogicalDriveStrings()
drive_options = drv.split('\000')[:-1]

#drive_options = ['C:', 'D:', 'E:', 'F:', 'G:']
drived = StringVar()
drived.set('Drive')
drop_driv = OptionMenu(guiapk,drived,*drive_options)
drop_driv.config(bg='lightsteelblue',font='lato 10 bold')

# create a label
label_path = tk.Label(guiapk,text='Enter Path',font='lato 12 bold',padx='10',pady='10',bg='lightsteelblue')
label_ext = tk.Label(guiapk,text='Choose Extension',font='lato 12 bold',padx='10',pady='10',bg='lightsteelblue')
label_drv = tk.Label(guiapk,text='Choose Drive',font='lato 12 bold',padx='10',pady='15',bg='lightsteelblue')

#Create a entry box
entry_path = tk.Entry(guiapk,textvariable=path_var,font='lato 12 bold')
#entry_ext = tk.Entry(guiapk,textvariable = ext_var)

# creatw a button
sub_button = tk.Button(guiapk,text='Search',command=spec_path,font='lato 12 bold',bg='aquamarine',bd="5",padx='10',pady='3',relief='groove')
ref_button = tk.Button(guiapk,text='Reset',command=refresh,font='lato 12 bold',bg='khaki',bd="5",padx='10',pady='3',relief='groove')
cls_button = tk.Button(guiapk,text='Close',command=exit,font='lato 12 bold',bg='lightcoral',bd="5",padx='10',pady='3',relief='groove')

#placing label at right position

label_path.grid(row=0,column=0)
entry_path.grid(row=0,column=1)

label_ext.grid(row=1,column=0)
label_drv.grid(row=2,column=0)

#entry_ext.grid(row=1,column=2)

# # placing drop down at right position
drop.grid(row=1,column=1)
drop_driv.grid(row=2,column=1)

# placing buttons at right position
sub_button.grid(row=1,column=3,columnspan=2,sticky=N+S+E+W)
ref_button.grid(row=2,column=3,sticky=N+S+E+W)
cls_button.grid(row=2,column=4,sticky=N+S+E+W)

#create a output box
label_output = tk.Label(guiapk,text=' O U T P U T ',font='lato 12 bold',bg='grey',padx='10',pady='10',relief='groove')
label_output.grid(row=4,column=1,columnspan=2,padx='10',pady='10',sticky=N+S+E+W)

output = Text(guiapk,height=30,width=155,bg='lightslategrey',font='lato 12',fg='navy',padx='10',pady='5',relief='groove')
output.grid(row=6,columnspan=5)

guiapk.mainloop()