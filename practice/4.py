from ctypes.wintypes import MSG
from ftplib import MSG_OOB
import msilib
import sqlite3
from tkinter import StringVar
from tkinter.ttk import Widget


def __init__(self,master):
    self.master = master
    self.username = StringVar()
    self.password= StringVar()
    self.n_username =StringVar()
    self.n_password =StringVar()
    self ,Widget()

def new_user(self):
    with sqlite3.connect('user.db') as db:
        c= db.cursor()
    find_user = ('SELECT * FROM user WHERE username = ?')
    c.execute(find_user,[(self.username.get())])
    if c.fetchall():
        msilib.showerror('Error!','username Already taken!')
    else:
        msilib.MSIMODIFY_VALIDATE_FIELD.showinfo('sucess!','Account created!')
        self.log()
    insert ='INSERT INTO user(username,password) VALUES(?,?)'
    c.execute(insert,[(self.n_username.get()),(self.n_password.get())])
    db.commit()