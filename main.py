from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from criminal import Criminal
import os


class criminal_detection_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("CRIMINAL DETECTION SYSTEM")
        
        
        lbl_title=Label(self.root,text='CRIMINAL DETECTION  SYSTEM ',font=('times new roman',40,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1530,height=70)
        
        
        img=Image.open("IMAGES/background.png")
        img=img.resize((1530,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=70,width=1530,height=720)
        
        #windows
         
        img1=Image.open("IMAGES/button1.png")
        img1=img1.resize((620,80),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(bg_img,image=self.photoimg1,command=self.criminal_details,cursor="hand2")
        b1.place(x=440,y=50,width=620,height=60)
        
        b_1=Button(b1,text="CRIMINAL REGISTRATION",command=self.criminal_details,cursor="hand2",font=('times new roman',16,'bold'),bg='white',fg='black')
        b_1.place(x=155,y=7,width=300,height=40)
        
        
        
         #windows2
         
        img2=Image.open("IMAGES/button2.png")
        img2=img2.resize((620,80),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
         
        b2=Button(bg_img,image=self.photoimg2,cursor="hand2")
        b2.place(x=440,y=140,width=620,height=60)
        
        b_2=Button(b2,text="FACE DETECTION",cursor="hand2",font=('times new roman',20,'bold'),bg='white',fg='black')
        b_2.place(x=155,y=7,width=300,height=40)
        
         #windows3
         
        img3=Image.open("IMAGES/button1.png")
        img3=img3.resize((620,80),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b3.place(x=440,y=230,width=620,height=60)
        
        b_3=Button(b3,text="TRAIN DATA",cursor="hand2",font=('times new roman',20,'bold'),bg='white',fg='black')
        b_3.place(x=155,y=7,width=300,height=40)
        
        #windows4
        img4=Image.open("IMAGES/button1.png")
        img4=img4.resize((620,80),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b4=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b4.place(x=440,y=325,width=620,height=60)
        
        b_4=Button(b4,text="CRIMINAL IDENTIFICATION",cursor="hand2",font=('times new roman',15,'bold'),bg='white',fg='black')
        b_4.place(x=155,y=7,width=300,height=40)
        
        #windows4
        img5=Image.open("IMAGES/button1.png")
        img5=img5.resize((620,80),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b5=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b5.place(x=440,y=422,width=620,height=60)
        
        b_5=Button(b5,text="CRIMINAL DATABASE",cursor="hand2",font=('times new roman',17,'bold'),bg='white',fg='black')
        b_5.place(x=155,y=7,width=300,height=40)
        
        
        #windows4
        img6=Image.open("IMAGES/button1.png")
        img6=img6.resize((620,80),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b6=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_img)
        b6.place(x=440,y=522,width=620,height=60)
        
        b_6=Button(b6,text="CRIMINAL IMAGE",cursor="hand2",command=self.open_img,font=('times new roman',17,'bold'),bg='white',fg='black')
        b_6.place(x=155,y=7,width=300,height=40)
        
        
    
    def open_img(self):
        os.startfile("data")
    
    
        
        
    def criminal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Criminal(self.new_window)
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=criminal_detection_system(root)
    root.mainloop()        