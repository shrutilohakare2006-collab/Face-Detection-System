from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI face recognition system")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",30,"bold"),bg='white',fg="#480B61")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        img_top=Image.open('help2.jpg')
        img_top=img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=720)

        dep_label=Label(f_label,text="Email:mayurishete001@gmail.com",font=("times new roman",20,"bold"),fg="maroon")
        dep_label.place(x=550,y=220)







if __name__=='__main__':
    root=Tk()
    obj=Help(root)
    root.mainloop()                