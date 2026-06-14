from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI face recognition system")
        
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

       

        img=Image.open('studimghead.jpg')
        img=img.resize((800,200),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=800,height=200)

        #image2
        img1=Image.open('studimghead.jpg')
        img1=img1.resize((800,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=800,y=0,width=800,height=200)

        img2=Image.open('facebg.jpg')
        img2=img2.resize((1530,710),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=0,y=140,width=1530,height=710)

          #title
        title_lbl=Label(f_label,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg='white',fg="#480B61")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        main_frame=Frame(f_label,bd=2)
        main_frame.place(x=20,y=55,width=1480,height=600)

        left_frame=LabelFrame(main_frame,bg='white',bd=2,relief=RIDGE,text="Studenta Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

         #left lable frame
        img_left=Image.open('leftstud.jpg')
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg='white')
        left_inside_frame.place(x=0,y=180,width=720,height=300)

#aid
        aid_label=Label(left_inside_frame,text="AttendanceID",font=("times new roman",12,"bold"))
        aid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studid_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        studid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #Student Name
        studname_label=Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"))
        studname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studname_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",13,"bold"))
        studname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Class Div
        classdiv_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"))
        classdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        studname_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",13,"bold"))
        studname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

       
         #Roll no
        rollno_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"))
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
         #Gender
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
      

       # gender_entry=ttk.Entry(current_stud_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #DOB
        dob_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        #attendance
        att_label=Label(left_inside_frame,text="Attendance",font=("times new roman",12,"bold"),bg='white')
        att_label.grid(row=3,column=0)
        self.att_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,width=20,font=("times new roman",12,"bold"),state="readonly")
        self.att_combo["values"]=("Status","Present","Absent")
        self.att_combo.current(0)
        self.att_combo.grid(row=3,column=1,pady=8,sticky=W)

      

         #buttonsframe
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=35)
      
      #save
        save_btn=Button(btn_frame,text="Import csv",width=17,command=self.import_csv,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        save_btn.grid(row=0,column=0,padx=2)

        update_btn=Button(btn_frame,text="Export CSV",width=17,command=self.export_csv,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        update_btn.grid(row=0,column=1,padx=2)

        delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        delete_btn.grid(row=0,column=2,padx=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        reset_btn.grid(row=0,column=3,padx=2)
 
        right_frame=LabelFrame(main_frame,bg='white',bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        
        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=5,y=0,width=720,height=130)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=710,height=445)
        

        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.Att_report_table=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Att_report_table.xview)
        scroll_y.config(command=self.Att_report_table.yview)

        self.Att_report_table.heading("id",text="AttendanceID")
        self.Att_report_table.heading("roll",text="Roll")
        self.Att_report_table.heading("name",text="Name")
        self.Att_report_table.heading("dep",text="Department")
        self.Att_report_table.heading("time",text="Time")
        self.Att_report_table.heading("date",text="Date")
        
        self.Att_report_table.heading("attendance",text="Attendance")
        self.Att_report_table["show"]="headings"
        self.Att_report_table.pack(fill=BOTH,expand=1)

        self.Att_report_table.column("id",width=100)
        self.Att_report_table.column("roll",width=100)
        self.Att_report_table.column("name",width=100)
        self.Att_report_table.column("dep",width=100)
        self.Att_report_table.column("time",width=100)
        self.Att_report_table.column("date",width=100)
        self.Att_report_table.column("attendance",width=100)

        self.Att_report_table.bind("<ButtonRelease>",self.get_cursor)

    def fetch_data(self,rows):    
        self.Att_report_table.delete(*self.Att_report_table.get_children())
        for i in rows:
            self.Att_report_table.insert("",END,values=i)
    def import_csv(self):
         global mydata
         mydata.clear()
    
         fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            parent=self.root
           )
         with open(fln)as myfile:
             csvread=csv.reader(myfile,delimiter=",")
             for i in csvread:
                 mydata.append(i)
             self.fetch_data(mydata)     
    def export_csv(self):    
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found",parent=self.root)   
                return False
            fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            parent=self.root
            )
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerows(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successful!!")

        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
        cursor_row=self.Att_report_table.focus()
        content=self.Att_report_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    def reset(self):
         self.var_atten_id.set("")
         self.var_atten_roll.set("")
         self.var_atten_name.set("")
         self.var_atten_dep.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance.set("")

        

        

if __name__=='__main__':
    root=Tk()
    obj=Attendance(root)
    root.mainloop()             