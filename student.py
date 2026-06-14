from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("AI face recognition system")
 
       #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       



       #image1
        img=Image.open('studimghead.jpg')
        img=img.resize((900,140),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=765,height=140)

        #image2
        img1=Image.open('studimghead.jpg')
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
        title_lbl=Label(f_label,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg='white',fg="#480B61")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        main_frame=Frame(f_label,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bg='white',bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        

        #left lable frame
        img_left=Image.open('leftstud.jpg')
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_label=Label(left_frame,image=self.photoimg_left)
        f_label.place(x=5,y=0,width=720,height=130)
        
        #current course frame
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","CS","AI","ML","Mechanical")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2)
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        sem_combo["values"]=("Select Semester","I","II","III","IV")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #current Student frame
        current_stud_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Student Information",font=("times new roman",12,"bold"))
        current_stud_frame.place(x=5,y=250,width=720,height=300)
        
        #Student id
        studid_label=Label(current_stud_frame,text="Student Id:",font=("times new roman",12,"bold"))
        studid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studid_entry=ttk.Entry(current_stud_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        studname_label=Label(current_stud_frame,text="Student Name:",font=("times new roman",12,"bold"))
        studname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studname_entry=ttk.Entry(current_stud_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Class Div
        classdiv_label=Label(current_stud_frame,text="Class Div:",font=("times new roman",12,"bold"))
        classdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(current_stud_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="read only")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
         #Roll no
        rollno_label=Label(current_stud_frame,text="Roll No:",font=("times new roman",12,"bold"))
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollno_entry=ttk.Entry(current_stud_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
         #Gender
        gender_label=Label(current_stud_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(current_stud_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

       # gender_entry=ttk.Entry(current_stud_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #DOB
        dob_label=Label(current_stud_frame,text="Date of Birth:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(current_stud_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
         #Email
        Email_label=Label(current_stud_frame,text="Email:",font=("times new roman",12,"bold"))
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(current_stud_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
       
        #phone no
        phno_label=Label(current_stud_frame,text="Phone No:",font=("times new roman",12,"bold"))
        phno_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phno_entry=ttk.Entry(current_stud_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phno_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
         #Address
        addr_label=Label(current_stud_frame,text="Address:",font=("times new roman",12,"bold"))
        addr_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        addr_entry=ttk.Entry(current_stud_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        addr_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
         #Teacher name
        tname_label=Label(current_stud_frame,text="Email:",font=("times new roman",12,"bold"))
        tname_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        tname_entry=ttk.Entry(current_stud_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        tname_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #Radio Button1
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(current_stud_frame,variable=self.var_radio1,text="Take photo sample:",value=YES)
        radiobtn1.grid(row=7,column=0)
        
        radiobtn2=ttk.Radiobutton(current_stud_frame,variable=self.var_radio1,text="No photo sample:",value=NO)
        radiobtn2.grid(row=7,column=1)
      
      #buttonsframe
        btn_frame=Frame(current_stud_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=200,width=715,height=35)
      
      #save
        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        save_btn.grid(row=0,column=0,padx=2)

        update_btn=Button(btn_frame,text="Update",width=17,command=self.update_data,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        update_btn.grid(row=0,column=1,padx=2)

        delete_btn=Button(btn_frame,text="Delete",width=17,command=self.delete_data,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        delete_btn.grid(row=0,column=2,padx=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        reset_btn.grid(row=0,column=3,padx=2)

        #buttonsframe
        btn_frame1=Frame(current_stud_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=0,y=235,width=715,height=35)

        takephoto_btn=Button(btn_frame1,text="Take photo sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        takephoto_btn.grid(row=1,column=0,padx=4)

        updatephoto_btn=Button(btn_frame1,text="Update Photo",width=35 ,font=("times new roman",13,"bold"),bg="#480B61",fg='white')
        updatephoto_btn.grid(row=1,column=1)



        #Right label Frame
        right_frame=LabelFrame(main_frame,bg='white',bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        #Right lable frame
        img_right=Image.open('studimageheader.jpg')
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_label=Label(right_frame,image=self.photoimg_right)
        f_label.place(x=5,y=0,width=720,height=130)

        #search system
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=120)

        search_label=Label(search_frame,text="Seach By:",font=("times new roman",15,"bold"),bg="red",fg="White")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=17,state="read only")
        search_combo["values"]=("Select","Roll_no","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="#480B61",fg='white')
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show All",width=12 ,font=("times new roman",12,"bold"),bg="#480B61",fg='white')
        showall_btn.grid(row=0,column=4)

        #Table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","Id","Name","Div","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="StudId")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Div",text="Division")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("Photo",text="Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

        #Function Declaration

    def add_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",user="root",password="#Root",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute(
                    "INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                    messagebox.showinfo("success","student details has been added succesfully",parent=self.root)
                except Exception as es:
                     messagebox.showerror("Error",f"due to:{str(es)}",parent=self.root) 
    #fetch data
    
                    
    def fetch_data(self):
                    conn=mysql.connector.connect(host="localhost",user="root",password="#Root",database="face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    data=my_cursor.fetchall()

                    if len(data)!=0:
                          self.student_table.delete(*self.student_table.get_children())  
                          for i in data:
                                self.student_table.insert("",END,values=i)  



                          conn.commit()
                    conn.close()               
                 
#get cursor
        
    def get_cursor(self,event=""):
          cursor_focus=self.student_table.focus()
          content=self.student_table.item(cursor_focus)
          data=content["values"]
          self.var_dep.set(data[0]),
          self.var_course.set(data[1]),
          self.var_year.set(data[2]),
          self.var_semester.set(data[3]),
          self.var_std_id.set(data[4]),
          self.var_std_name.set(data[5]),
          self.var_div.set(data[6]),
          self.var_roll.set(data[7]),
          self.var_gender.set(data[8]),
          self.var_dob.set(data[9]),
          self.var_email.set(data[10]),
          self.var_phone.set(data[11]),
          self.var_address.set(data[12]),
          self.var_teacher.set(data[13]),
          self.var_radio1.set(data[14])

    #update
    def update_data(self):
          if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are Required",parent=self.root)
          else:
               try:
                     Update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)

                     if Update>0:
                             conn=mysql.connector.connect(host="localhost",user="root",password="#Root",database="face")
                             my_cursor=conn.cursor()
                             my_cursor.execute(
     "update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
     (
        self.var_dep.get(),
        self.var_course.get(),
        self.var_year.get(),
        self.var_semester.get(),
        self.var_std_id.get(),      # Student_id
        self.var_std_name.get(),    # Name
        self.var_div.get(),
        self.var_roll.get(),
        self.var_gender.get(),
        self.var_dob.get(),
        self.var_email.get(),
        self.var_phone.get(),
        self.var_address.get(),
        self.var_teacher.get(),
        self.var_radio1.get(),
        self.var_std_id.get()       # WHERE Student_id
     ))
                     else:
                           if not Update:
                                 return
                     messagebox.showinfo("Success","student detail successfully updated!!",parent=self.root)
                     conn.commit()
                     self.fetch_data()
                     conn.close()
               except Exception as es:
                     messagebox.showerror("error:",f"due to:{str(es)}",parent=self.root)

    def delete_data(self):
          if self.var_std_id.get()=="":
                messagebox.showerror("Error","student Id must be Required..",parent=self.root)
          else:
                try:
                       delete=messagebox.askyesno("student delete page","Do you want to delete this student",parent=self.root)
                       if delete>0:
                             conn=mysql.connector.connect(host="localhost",user="root",password="#Root",database="face")
                             my_cursor=conn.cursor()
                             sql="delete from student where Student_id=%s"
                             val=(self.var_std_id.get(),)
                             my_cursor.execute(sql,val)
                       else:
                             if not delete:
                                   return
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("delete","Succesfully deleted student Details",parent=self.root)
                                 


                except Exception as es:
                      messagebox.showerror("error:",f"due to:{str(es)}",parent=self.root)


#reset
    def reset_data(self):
          self.var_dep.set("select department")
          self.var_course.set("select course"),
          self.var_year.set("select year"),
          self.var_semester.set("select semester"),
          self.var_std_id.set(""),
          self.var_std_name.set(""),
          self.var_div.set("select division"),
          self.var_roll.set(""),
          self.var_gender.set("select gender"),
          self.var_dob.set(""),
          self.var_email.set(""),
          self.var_phone.set(""),
          self.var_address.set(""),
          self.var_teacher.set(""),
          self.var_radio1.set("")

 # Generate dataset and take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="#Root",
                    database="face"
                )

                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()

                id = 0
                for x in myresult:
                    id += 1

                my_cursor.execute(
                    """update student set
                    Dep=%s,
                    Course=%s,
                    Year=%s,
                    Semester=%s,
                    Student_id=%s,
                    Name=%s,
                    Division=%s,
                    Roll=%s,
                    Gender=%s,
                    Dob=%s,
                    Email=%s,
                    Phone=%s,
                    Address=%s,
                    Teacher=%s,
                    PhotoSample=%s
                    where Student_id=%s""",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )
                )

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on frontal face from OpenCV
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0

                while True:
                    ret, my_frame = cap.read()

                    if face_cropped(my_frame) is not None:
                        img_id += 1

                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                        file_name_path = f"data/user.{id}.{img_id}.jpg"

                        cv2.imwrite(file_name_path, face)

                        cv2.putText(
                            face,
                            str(img_id),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2
                        )

                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo(
                    "Result",
                    "Generating dataset completed",
                    parent=self.root
                )

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Due To : {str(es)}",
                    parent=self.root
                )
if __name__=='__main__':
    root=Tk()
    obj=Student(root)
    root.mainloop()       