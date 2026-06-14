from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter
import datetime
from time import strftime

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI face recognition system")

       #image1
        img=Image.open('faceheader2.jpg')
        img=img.resize((900,140),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=765,height=140)

        #image2
        img1=Image.open('faceheader1.jpg')
        img1=img1.resize((900,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=765,y=0,width=765,height=140)

        #bg
        img2=Image.open('facebg.jpg')
        img2=img2.resize((1530,710),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=0,y=140,width=1530,height=710)
      
        #title
        title_lbl=Label(f_label,text="AI FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg='white',fg='#00008B')
        title_lbl.place(x=0,y=0,width=1530,height=40)

 
        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),bg='white',fg='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        #student button
        img4=Image.open('studface.jpeg')
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(f_label,image=self.photoimg4,command=self.stud_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Student Details",command=self.stud_details,cursor="hand2",font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=200,y=300,width=220,height=40)
    
        #Detect face
        img5=Image.open('facebtn.jpg')
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(f_label,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=500,y=300,width=220,height=40)
   
      #attendance
        img6=Image.open('facedetectbtn.jpg')
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(f_label,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=800,y=300,width=220,height=40)

      #help face button
        img7=Image.open('helpdesk.jpg')
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(f_label,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=1100,y=300,width=220,height=40)

         #train
        img8=Image.open('trainbtn.jpg')
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(f_label,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Train",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=200,y=580,width=220,height=40)
    
      #photos
        img9=Image.open('photobtn.webp')
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(f_label,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=500,y=580,width=220,height=40)  
     
       #developer
        img10=Image.open('developerbtn.jpg')
        img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(f_label,image=self.photoimg10,cursor="hand2",command=self.dev_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Developer",cursor="hand2",command=self.dev_data,font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=800,y=580,width=220,height=40)  
       #Exit
        img11=Image.open('exitbtn.jpg')
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(f_label,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_lbl=Button(f_label,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg='white',fg='#00008B')
        b1_lbl.place(x=1100,y=580,width=220,height=40)  
     
    def open_img(self):
        os.startfile("data")
    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition", "are you sure exit these project",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return    






        


    #function button
    def stud_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)  
       
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)  

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)     
  
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def dev_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

      


if __name__=='__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()