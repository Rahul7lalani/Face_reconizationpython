from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 as cv
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition")

        # vaibles **************
        list =["Dep","Course","Year","Sem","Sid","Sname","Gender","Email","Phonenumber","DoB"]

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_div=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        img = Image.open(r"C:\Users\Admin\Downloads\woman-head-face-recognition-technology-close-up-beautiful-interface-network-hologram-concept-ai-machine-learning-toned-150583225.jpg")
        img = img.resize((510,130),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg =ImageTk.PhotoImage(img)
#
        f_lbl = Label(self.root,image=self.photoimg) # lable of image 
        f_lbl.place(x=0,y=0,width=510,height=130) # showing the image using placing
        #
        img1 = Image.open(r"C:\Users\Admin\Downloads\face-recognition-technology-closeup-man-108171249.jpg")
        img1 = img1.resize((510,130),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg1 =ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=130)

        #third image
        img2 = Image.open(r"C:\Users\Admin\Downloads\Facial-Recognition.jpg")
        img2 = img2.resize((510,130),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg2 =ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=130)


        #bg image
        img3 = Image.open(r"C:\Users\Admin\Downloads\face-recognition-low-poly-wireframe-banner-template-futuristic-computer-technology-smart-identification-system-poster-polygonal-design-facial-scan-3d-mesh-art-with-connected-dots_201274-4.webp")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg3 =ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl =Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg ="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)

         # WE NEED TO CREATE A FRAME HERE 

        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        #left  LABLE frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",13,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_2 = Image.open(r"C:\Users\Admin\Downloads\woman-head-face-recognition-technology-close-up-beautiful-interface-network-hologram-concept-ai-machine-learning-toned-150583225.jpg")
        img_2 = img2.resize((720,130),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg_2 =ImageTk.PhotoImage(img_2)

        f_lbl = Label(Left_frame,image=self.photoimg_2)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #current course
        CurrentCourse_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",13,"bold"))
        CurrentCourse_frame.place(x=5,y=130,width=720,height=120)


        dep_lable =Label(CurrentCourse_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo =ttk.Combobox(CurrentCourse_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=22,state="read only")
        dep_combo["values"]=("Select Department","CS","Electrical","IT","Civil","Mechanical","chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #courses
        course_lable =Label(CurrentCourse_frame,text="Courses",font=("times new roman",13,"bold"),bg="white")
        course_lable.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(CurrentCourse_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=22,state="read only")
        course_combo["values"]=("Select Course","FE","MTECH","FE","BTECH","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_lable =Label(CurrentCourse_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_lable.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(CurrentCourse_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=22,state="read only")
        year_combo["values"]=("Select YYear","2020","2021","2022","2023","2024","2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_lable =Label(CurrentCourse_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        semester_lable.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo = ttk.Combobox(CurrentCourse_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=22,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        


        #######################
        #Class Student Information Frame
        classstudent_frame=LabelFrame(master=Left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("chalkduster",12,"bold"),bg="skyblue",fg="purple")
        classstudent_frame.place(x=5,y=250,width=720,height=300)
        
        #Student Id
        studentid_label=Label(classstudent_frame,text="Student ID",font=("chalkduster",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studentid_entry = ttk.Entry(classstudent_frame,textvariable=self.var_id,width=15,font=("chalkduster",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #Student name
        studentname_label=Label(classstudent_frame,text="Name",font=("chalkduster",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        studentname_entry = ttk.Entry(classstudent_frame,textvariable=self.var_name,width=15,font=("chalkduster",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #Student Gender
        Gender_label=Label(classstudent_frame,text="Gender",font=("chalkduster",12,"bold"),bg="white")
        Gender_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(classstudent_frame,textvariable=self.var_gender,font=("chalkduster",12,"bold"),width=15,state="read only")
        gender_combo["values"]=("select Gender:","Male","Female","others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #Student email
        email_label=Label(classstudent_frame,text="E-mail",font=("chalkduster",12,"bold"),bg="white")
        email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        email_entry = ttk.Entry(classstudent_frame,textvariable=self.var_email,width=15,font=("chalkduster",12,"bold"))
        email_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #Student phone number
        phoneno_label=Label(classstudent_frame,text="Phone Number",font=("chalkduster",12,"bold"),bg="white")
        phoneno_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        phoneno_entry = ttk.Entry(classstudent_frame,textvariable=self.var_phone,width=15,font=("chalkduster",12,"bold"))
        phoneno_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)
        
        #Date-of-Birth
        dob_label=Label(classstudent_frame,text="Date-of-Birth",font=("chalkduster",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dob_entry = ttk.Entry(classstudent_frame,textvariable=self.var_dob,width=15,font=("chalkduster",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Radiobuttons
        self.var_radio1=StringVar()
        radiobutton1= ttk.Radiobutton(classstudent_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobutton1.grid(row=3,column=0,padx=2,pady=5)
        
        radiobutton2= ttk.Radiobutton(classstudent_frame,variable=self.var_radio1,text="NO Photo Sample",value="No")
        radiobutton2.grid(row=3,column=1,padx=2,pady=5)


        # Buttons Frame
        btn_frame = Frame(classstudent_frame,bd=2,relief=RIDGE,bg="light green")
        btn_frame.place(x=0,y=160,width=715,height=200)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,height=2 ,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,height=2 ,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,height=2 ,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        delete_btn.grid(row=0,column=2)

        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,height=2 ,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        Reset_btn.grid(row=0,column=3)

        Take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Sample",width=17,height=3,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        Take_photo_btn.grid(row=1,column=1)

        Update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=17,height=3,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        Update_photo_btn.grid(row=1,column=2)

############################################################
        #Right Frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("chalkduster",12,"bold"),bg="pink",fg="purple")
        right_frame.place(x=750,y=10,width=720,height=580)

        #search frame
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("chalkduster",12,"bold"),bg="yellow",fg="purple")
        search_frame.place(x=2,y=10,width=580,height=75)

        search_label=Label(search_frame,text="Search by:",font=("chalkduster",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("chalkduster",12,"bold"),width=10,state="read only")
        search_combo["values"]=("select :","Student ID","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10)

        search_entry = ttk.Entry(search_frame,width=15,font=("chalkduster",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,height=3,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Showall",width=10,height=3,font=("chalkduster",12,"bold"),bg="skyblue",fg="green")
        showall_btn.grid(row=0,column=4,padx=4)


        ##table farme
       #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="lightgreen")
        table_frame.place(x=2,y=100,width=580,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","Sid","Sname","Gender","Email","Phonenumber","DoB","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        for j in list:
            self.student_table.heading(j,text=j)
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        for j in list:
            self.student_table.column(j,width=100)
        self.student_table.column("Photo",width=150)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        

    #**************************************** function declaration*********************#

    def add_data(self):
        if self.var_dep.get()=="Select Department:" or self.var_id.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root) 
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rahul0605@#!",database="face_reco")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into new_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            self.var_id.get(),
                                                            self.var_name.get(),
                                                            self.var_gender.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_dob.get(),
                                                            self.var_radio1.get()
                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student added",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)} ",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rahul0605@#!",database="face_reco")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from new_table")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 
    ##########################
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_email.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_radio1.set(data[10])


    def update_data(self):
        if self.var_dep.get()=="Select Department":
            messagebox.showerror("Error", "All fields are required",parent=self.root) 
        else:
            try:
                Update=messagebox.askyesno("Update","Do you wanna update",parent=self.root)
                if  Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rahul0605@#!",database="face_reco")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update new_table set Dep=%s,Course=%s,Year=%s,Sem=%s,Sname=%s,Gender=%s,Email=%s,Phonenumber=%s,DoB=%s,Photo=%s where Sid=%s",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            self.var_name.get(),
                                                            self.var_gender.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_dob.get(),
                                                            self.var_radio1.get(),
                                                            self.var_id.get()           

                                                     ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Update complete",parent = self.root)         
                conn.commit()
                self.fetch_data()
                conn.close()
    
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Sid required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rahul0605@#!",database="face_reco")
                    my_cursor=conn.cursor()
                    val=(self.var_id.get(),)
                    my_cursor.execute("delete from new_table where Sid=%s",val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","deleted sucessfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}", parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select YYear"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_gender.set("select Gender:"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_dob.set(""),
        self.var_radio1.set("")
            
            
    #====================== Generate data set or Take data sample===========================================
    def generate_dataset(self):
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rahul0605@#!",database="face_reco")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from new_table")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update new_table set Dep=%s,Course=%s,Year=%s,Sem=%s,Sname=%s,Gender=%s,Email=%s,Phonenumber=%s,DoB=%s,Photo=%s where Sid=%s",(
                                                            self.var_dep.get(),
                                                            self.var_course.get(),
                                                            self.var_year.get(),
                                                            self.var_semester.get(),
                                                            self.var_name.get(),
                                                            self.var_gender.get(),
                                                            self.var_email.get(),
                                                            self.var_phone.get(),
                                                            self.var_dob.get(),
                                                            self.var_radio1.get(),
                                                            self.var_id.get() ==id+1           

                                                        ))  

                conn.commit()  
                self.fetch_data()
                self.reset_data()
                conn.close()    


                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                capture=cv2.VideoCapture(0)
                image_id=0
                while True:
                    ret, my_frame=capture.read()
                    if face_cropped(my_frame) is not None:
                        image_id+=1
                        face=cv.resize(face_cropped(my_frame),(450,450))
                        face=cv.cvtColor(face,cv.COLOR_BGR2GRAY)
                        File_path="data/user."+str(id)+"."+str(image_id)+".jpg"
                        cv.imwrite(File_path,face)
                        cv.putText(face,str(image_id),(50,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv.imshow("Cropped Face",face)
                         
                    if cv.waitKey(1)==13 or int(image_id)==100:
                        break
                capture.release()
                cv.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Competed!",parent=self.root)    
            
            
            
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{es}",parent=self.root)
            



if __name__ == "__main__" :
    root =Tk()
    #object of a class
    obj=Student(root)
    #closing loop
    root.mainloop()

 