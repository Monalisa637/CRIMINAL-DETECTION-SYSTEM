from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from criminal import Criminal
import os
import cv2
import mysql.connector
import numpy as np 
from tkinter import messagebox
import requests
from gmail import facerecognition


class criminal_detection_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("CRIMINAL DETECTION SYSTEM")
        
        
        lbl_title=Label(self.root,text='CRIMINAL DETECTION  SYSTEM ',font=('times new roman',40,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1530,height=70)
        
        
        img=Image.open("IMAGES/background.png")
        img=img.resize((1530,720),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=70,width=1530,height=720)
        
        #windows
         
        img1=Image.open("IMAGES/button1.png")
        img1=img1.resize((620,80),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(bg_img,image=self.photoimg1,command=self.criminal_details,cursor="hand2")
        b1.place(x=50,y=200,width=620,height=60)
        
        b_1=Button(b1,text="CRIMINAL REGISTRATION",command=self.criminal_details,cursor="hand2",font=('times new roman',16,'bold'),bg='white',fg='black')
        b_1.place(x=155,y=7,width=300,height=40)
        
        
        
         #windows2
         
        img2=Image.open("IMAGES/button2.png")
        img2=img2.resize((620,80),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
         
        b2=Button(bg_img,image=self.photoimg2,command=self.face_identification,cursor="hand2")
        b2.place(x=50,y=280,width=620,height=60)
        
        b_2=Button(b2,text="CRIMINAL IDENTIFICATION",command=self.face_identification,cursor="hand2",font=('times new roman',16,'bold'),bg='white',fg='black')
        b_2.place(x=155,y=7,width=300,height=40)
        
         #windows3
         
        img3=Image.open("IMAGES/button1.png")
        img3=img3.resize((620,80),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.open_img)
        b3.place(x=50,y=360,width=620,height=60)
        
        b_3=Button(b3,text="CRIMINAL DATABASE",command=self.open_img,cursor="hand2",font=('times new roman',16,'bold'),bg='white',fg='black')
        b_3.place(x=155,y=7,width=300,height=40)
        
        
        
        
        
        img5=Image.open("IMAGES/backgroung1.png")
        img5=img5.resize((550,550),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        bg_img5=Label(self.root,image=self.photoimg5)
        bg_img5.place(x=800,y=140,width=550,height=550)
        
        
        
        
        
        
        
        
    def open_img(self):
        os.startfile("data")
        
       
        
        
    
    def criminal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Criminal(self.new_window)
        
        
    
    def face_identification(self):
        self.new_window=Toplevel(self.root)
        self.app=facerecognition(self.new_window)  
    

  
    
                        
        
        
        
        
        
            

        
if __name__=="__main__":
    root=Tk()
    obj=criminal_detection_system(root)
    root.mainloop()        