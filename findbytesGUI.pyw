import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

def oldexefs():
    oldfile = tk.filedialog.askopenfilename(title="移植元のバージョンのファイルを選択")
    oldfileL['text'] = oldfile
    
def newexefs():
    newfile = tk.filedialog.askopenfilename(title="最新のバージョンのファイルを選択")
    newfileL['text'] = newfile
    
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
    oldfile = oldfileL.cget("text")
    newfile= newfileL.cget("text")
    cmd = "python findbytes.py" + " " + oldfile + " " + newfile  + " " + oldcode
    print(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    ncode = p.stdout.read()
    print(ncode)
    newipscode.insert(tk.END,ncode)
    newipscode.configure(state='readonly')

root = tk.Tk()
root.geometry('720x500')
root.title("findbytesGUI")
root.resizable(False, False)
resetbutton = tk.Button(root, text = 'リセット', height = 3, command = reset).pack(fill = 'x', padx = 20, pady = 20, side = 'bottom')
findbutton = tk.Button(root, text = '移植', height = 5, command = port).pack(fill = 'x', padx = 20, pady = 20, side = 'bottom')
oldipscode = tk.Entry(root)
oldipscode.place(x = 10, y = 180, height = 100, width = 345)
newipscode = tk.Entry(root)
newipscode.place(x = 365, y = 180, height = 100, width = 345)
newipscode.configure(state='readonly')
oldcode = tk.Label(text='古いオフセット')
oldcode.place(x=10, y=155)
newcode = tk.Label(text='新しいオフセット')
newcode.place(x=365, y=155)
oldfilebutton = tk.Button(root, text = '移植元のファイル', command = oldexefs)
oldfilebutton.place(x=10, y=25)
newfilebutton = tk.Button(root, text = '最新のファイル', command = newexefs)
newfilebutton.place(x=10, y=85)
oldfileL = tk.Label()
oldfileL.place(x=120, y=25)
newfileL = tk.Label()
newfileL.place(x=120, y=85)
root.mainloop()
