from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('Data Training')
        
        
        lbl_title=Label(self.root,text=' TRAINED CRIMINAL IMAGE ',font=('times new roman',40,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1530,height=70)   
        
        
        
        img=Image.open("IMAGES/background.png")
        img=img.resize((1530,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=70,width=1530,height=720)
        
        
        
        #train buttons
        img3=Image.open("IMAGES/button1.png")
        img3=img3.resize((620,80),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b3.place(x=20,y=300,width=620,height=60)
        
        b_3=Button(b3,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=('times new roman',20,'bold'),bg='white',fg='black')
        b_3.place(x=155,y=7,width=300,height=40)
        
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        
        for image in path:
            img=Image.open(image).convert('L')    #gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        
        #train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")    
            
            
                       
        
        
        
        
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()                   
                            
           