#from distutils.dep_util import newer_pairwise
from tkinter import*
from tkinter import ttk
#from turtle import title, width
from PIL import Image,ImageTk
from student import Student
import os
import tkinter
from tkinter import messagebox
from train import Train
from face_reconization import Face_recognition
from attendence import Attendence
from developer import Developer
from help import Help
# above are the important libraies for our project


class Face_Recognition_System: 
    #calling constructor here init is termed as initilization
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #width and height and 0 and 0 represent x and y axis
        self.root.title("face recognition") # title

        # to open pathj of image and we need to copy the path of the image here and below we also set the size of image 
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

        title_lbl =Label(bg_img,text="Face Recongination Attendence System Software",font=("times new roman",35,"bold"),bg ="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # button
        img4 = Image.open(r"C:\Users\Admin\Downloads\successful-college-student-lg.png")
        img4 = img4.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg4 =ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image=self.photoimg4,command = self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student details",command = self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg ="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)

         # button
        img5 = Image.open(r"C:\Users\Admin\Downloads\facial-recognition-system-concept-young-man-street-face-104779649.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg5 =ImageTk.PhotoImage(img5)

        b2 = Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg ="white",fg="red")
        b2_1.place(x=500,y=300,width=220,height=40)


         # button
        img6 = Image.open(r"C:\Users\Admin\Downloads\image1-4.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg6 =ImageTk.PhotoImage(img6)

        b3 = Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attemdence_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1 = Button(bg_img,text="Attendence",cursor="hand2",command=self.attemdence_data,font=("times new roman",15,"bold"),bg ="white",fg="red")
        b3_1.place(x=800,y=300,width=220,height=40)


         # button
        img7 = Image.open(r"C:\Users\Admin\Downloads\4939493.png")
        img7 = img7.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg7 =ImageTk.PhotoImage(img7)

        b4 = Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.Help_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1 = Button(bg_img,text="Help desk",cursor="hand2",command=self.Help_data,font=("times new roman",15,"bold"),bg ="white",fg="red")
        b4_1.place(x=1100,y=300,width=220,height=40)
        


        img8 = Image.open(r"C:\Users\Admin\Downloads\woman-head-face-recognition-technology-hud-beautiful-dark-hair-interface-network-hologram-concept-ai-machine-learning-150583105.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg8 =ImageTk.PhotoImage(img8)

        b5 = Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1 = Button(bg_img,text="Train dataset",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg ="white",fg="red")
        b5_1.place(x=200,y=580,width=220,height=40)

         # button
        img9 = Image.open(r"C:\Users\Admin\Downloads\downloadtiiruf.jpeg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg9 =ImageTk.PhotoImage(img9)

        b6 = Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1 = Button(bg_img,text="Photos collection",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg ="white",fg="red")
        b6_1.place(x=500,y=580,width=220,height=40)


         # button
        img10 = Image.open(r"C:\Users\Admin\Downloads\downloaddfsdfdz.jpeg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg10 =ImageTk.PhotoImage(img10)

        b7 = Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)

        b7_1 = Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",15,"bold"),bg ="white",fg="red")
        b7_1.place(x=800,y=580,width=220,height=40)


         # button
        img11 = Image.open(r"C:\Users\Admin\Downloads\dsfsrfsgsg.jpeg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)#antilias convert high level image to low level
        self.photoimg11 =ImageTk.PhotoImage(img11)

        b8 = Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",15,"bold"),bg ="white",fg="red")
        b8_1.place(x=1100,y=580,width=220,height=40)
        ### function button

    def open_img(self):
        os.startfile("data")

    def iexit(self):
        self.iexit=messagebox.askyesno("Exit","Thank you for using this Project::Are you Sure you wanna exit",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return 

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attemdence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)   

    def Help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)  


if __name__ == "__main__" :
    root =Tk()
    #object of a class
    obj=Face_Recognition_System(root)
    #closing loop
    root.mainloop()
