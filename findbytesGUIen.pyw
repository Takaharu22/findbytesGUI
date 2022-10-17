import subprocess
import sys
import os
import tkinter as tk
from tkinter import filedialog

def oldexefs():
    oldfile = tk.filedialog.askopenfilename(title = "old exefs")
    oldfileL['text'] = oldfile
    
def newexefs():
    newfile = tk.filedialog.askopenfilename(title = "new exefs")
    newfileL['text'] = newfile
    
def inpchtxt():
    pchtxt = tk.filedialog.askopenfilename(title = "pchtxt")
    pchtxtfileL['text'] = pchtxt
    
def reset():
    newipscode.configure(state='normal')
    oldipscode.delete(0, tk.END)
    newipscode.delete(0, tk.END)
    newipscode.configure(state='readonly')
    
def port():
    newipscode.configure(state='normal')
    oldcode = oldipscode.get()
    oldipscode.delete(0, tk.END)
    newipscode.delete(0, tk.END)
    oldipscode.insert(tk.END,oldcode)
    oc = oldcode[:8]
    oldfile = oldfileL.cget("text")
    newfile = newfileL.cget("text")
    cmd = "python findbytes.py" + " " + oldfile + " " + newfile  + " " + oc
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ncode = p.stdout.read()
    new = f'{ncode[:8]}' + " " + f'{oldcode[9:]}'
    newcode = new.replace("'", '')
    newco = newcode.replace("b", '')
    newipscode.insert(tk.END,newco)
    newipscode.configure(state='readonly')
    
def portpchtxt():
    pchtxt = pchtxtfileL.cget("text")
    oldfile = oldfileL.cget("text")
    newfile = newfileL.cget("text")
    f = open(pchtxt, 'r', encoding='UTF-8')
    while True:
        data = f.readline()
        if data == '':
            break
        else:
            if ' ' in data:
                if data.find(' ') == 8:
                    oc = data[:8]
                    value = data[8:]
                    cmd = "python findbytes.py" + " " + oldfile + " " + newfile  + " " + oc
                    print(cmd)
                    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                    ncode = p.stdout.read()
                    new = f'{ncode[:8]}' + f'{value}'
                    newcode = new.replace("'", '')
                    newco = newcode.replace("b", '')
                    fn = open("new.pchtxt", 'a', encoding='UTF-8')    
                    fn.write(newco)
                else:
                    fn = open("new.pchtxt", 'a', encoding='UTF-8')    
                    fn.write(data)
            else:
                fn = open("new.pchtxt", 'a', encoding='UTF-8')    
                fn.write(data)
    f.close()
    fn.close()
    
root = tk.Tk()
root.geometry('720x500')
root.title("findbytesGUI")
root.resizable(False, False)
resetbutton = tk.Button(root, text = 'reset', height = 3, command = reset).pack(fill = 'x', padx = 20, pady = 20, side = 'bottom')
findbutton = tk.Button(root, text = 'port', height = 5, command = port).pack(fill = 'x', padx = 20, pady = 20, side = 'bottom')
oldipscode = tk.Entry(root)
oldipscode.place(x = 10, y = 180, height = 100, width = 345)
newipscode = tk.Entry(root)
newipscode.place(x = 365, y = 180, height = 100, width = 345)
newipscode.configure(state='readonly')
oldcode = tk.Label(text='old offset')
oldcode.place(x=10, y=155)
newcode = tk.Label(text='new offset')
newcode.place(x=365, y=155)
oldfilebutton = tk.Button(root, text = 'old exefs', command = oldexefs)
oldfilebutton.place(x=10, y=25)
newfilebutton = tk.Button(root, text = 'new exefs', command = newexefs)
newfilebutton.place(x=10, y=85)
pchtxtbutton = tk.Button(root, text = 'pchtxt', command = inpchtxt)
pchtxtbutton.place(x=370, y=25)
pchtxtbutton = tk.Button(root, text = 'port pchtxt', command = portpchtxt)
pchtxtbutton.place(x=370, y=85)
oldfileL = tk.Label()
oldfileL.place(x=100, y=25)
newfileL = tk.Label()
newfileL.place(x=90, y=85)
pchtxtfileL = tk.Label()
pchtxtfileL.place(x=420, y=25)
root.mainloop()