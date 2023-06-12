# CRIMINAL-DETECTION-SYSTEM
It is a crime detection based webapp using ai/ml and computer vision
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
        
    #vaeiables
    
        self.var_caseid=StringVar()
        self.var_criminalno=StringVar()
        self.var_dateofcrime=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_criminalname=StringVar()
        self.var_status=StringVar()
        self.var_address=StringVar()
        self.var_criminaltype=StringVar()        
        
            
        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM ',font=('times new roman',40,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1530,height=70)       
        
        # ncr logo 
        img_logo=Image.open('IMAGES/logo.png')
        img_logo=img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=200,y=5,width=60,height=60)
        
        # Img_Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=150)
        
        img1=Image.open('IMAGES/law.png')
        img1=img1.resize((1530,200),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        
        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=1530,height=150)
        
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=0,y=225,width=1530,height=570)
        
        
        # upper Frame
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL INFORMATION ',font=('times new roman',20,'bold'),fg='black')
        upper_frame.place(x=0,y=0,width=1530,height=340)
        
        #label entry
        
        #case id
        caseid=Label(upper_frame,text='case ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)
        
        caseentry=ttk.Entry(upper_frame,textvariable= self.var_caseid,width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)
        
        #criminal no
        lbl_criminal_no=Label(upper_frame,text='criminal NO:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_no.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminalno,width=22,font=('arial',11,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=2,pady=7,sticky=W)
        
         #criminal type
        lbl_criminal_type=Label(upper_frame,text='criminal Type:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_type.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        
        txt_criminal_type=ttk.Entry(upper_frame,textvariable= self.var_criminaltype,width=22,font=('arial',11,'bold'))
        txt_criminal_type.grid(row=1,column=5,padx=2,pady=7,sticky=W)
        
       
         #criminal name
        lbl_criminal_name=Label(upper_frame,text='criminal Name:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_name.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        txt_criminal_name=ttk.Entry(upper_frame,textvariable=self.var_criminalname,width=22,font=('arial',11,'bold'))
        txt_criminal_name.grid(row=0,column=5,padx=2,pady=7,sticky=W)
        
        
         #criminal Address
        lbl_criminal_address=Label(upper_frame,text=' Address:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_address.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        txt_criminal_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_criminal_address.grid(row=2,column=5,padx=2,pady=7,sticky=W)
        
         #criminal gender
        lbl_criminal_gender=Label(upper_frame,text='Gender:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_gender.grid(row=1,column=0,padx=5,pady=2,sticky=W)
        
        txt_criminal_gender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=('arial',11,'bold'))
        txt_criminal_gender.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        
        #criminal age
        lbl_criminal_age=Label(upper_frame,text='Age:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_age.grid(row=1,column=2,padx=5,pady=2,sticky=W)
        
        txt_criminal_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',11,'bold'))
        txt_criminal_age.grid(row=1,column=3,padx=5,pady=2,sticky=W)
        
         #criminal doa
        lbl_criminal_date1=Label(upper_frame,text='Arrest Date:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_date1.grid(row=2,column=0,padx=5,pady=2,sticky=W)
        
        txt_criminal_date1=ttk.Entry(upper_frame,textvariable= self.var_dateofcrime,width=22,font=('arial',11,'bold'))
        txt_criminal_date1.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
         
         #criminal status
        lbl_criminal_status=Label(upper_frame,text='Status:',font=('arial',11,'bold'),bg='white')
        lbl_criminal_status.grid(row=2,column=2,padx=5,pady=2,sticky=W)
        
        txt_criminal_status=ttk.Entry(upper_frame,textvariable=self.var_status,width=22,font=('arial',11,'bold'))
        txt_criminal_status.grid(row=2,column=3,padx=5,pady=2,sticky=W)
        
        
        #buttons
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        Button_frame.place(x=5,y=130,width=536,height=82)
        
        #add
        btn_add=Button(Button_frame,text="Save",command=self.add_data,font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_add.grid(row=0,column=0,padx=3,pady=3)
        
        #update
        btn_update=Button(Button_frame,command=self.update_data,text="Update",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_update.grid(row=0,column=1,padx=3,pady=3)
        
        
        #clear
        btn_clear=Button(Button_frame,command=self.clear_data,text="Clear",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_clear.grid(row=0,column=2,padx=3,pady=3)
        
        #delete
        btn_delet=Button(Button_frame,command=self.delete_data,text="Delete",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_delet.grid(row=0,column=3,padx=3,pady=3)
        
        #take photo
        
        btn_take=Button(Button_frame,command=self.generate_dataset,text="Take Photo",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_take.grid(row=1,column=0,padx=3,pady=3)
        
        
        
         #update photo
        btn_update1=Button(Button_frame,text="Update Photo",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_update1.grid(row=1,column=1,padx=3,pady=3)
        
        
        
         #train photo
        
        btn_train=Button(Button_frame,command=self.train_classifier,text="Train photo",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_train.grid(row=1,column=2,padx=3,pady=3)
        
        
        
        
         #camera
        camera_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='Black')
        camera_frame.place(x=950,y=0,width=550,height=265)
        
        #cameratext
        lbl_criminal_criminal=Label(camera_frame,text='CAMERA',font=('arial',11,'bold'),bg='Blue')
        lbl_criminal_criminal.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        
        
       
        
        
        
        
        # Lower Frame
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='CRIMINAL RECORD',font=('times new roman',15,'bold'),fg='black')
        down_frame.place(x=0,y=300,width=1530,height=260)
        
        # search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='SEARCH',font=('times new roman',15,'bold'),fg='black')
        search_frame.place(x=0,y=0,width=1530,height=60)
        
        
        search_by=Label(search_frame,text='Search',font=('arial',11,'bold'),bg='black',fg="white")
        search_by.grid(row=0,column=0,padx=5,sticky=W)
        
        self.var_com_search=StringVar()
        bo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("arial","11","bold"),width=18,state='readonly')
        bo_search_box['value']=('Select option','caseid','criminalNo')
        bo_search_box.current(0)
        bo_search_box.grid(row=0,column=1,padx=5,sticky=W)  
        
        
        self.var_search=StringVar() 
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5,sticky=W)
        
        btn_search=Button(search_frame,command=self.serch_data,text="Search",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_search.grid(row=0,column=3,padx=3)
        
        btn_all=Button(search_frame,command=self.detch_data,text="Show All",font=('arial',11,'bold'),bg='black',width=13,fg="white",height="1")
        btn_all.grid(row=0,column=4,padx=3)
        
        
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1500,height="140")
        
        Scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
         
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        
        Scroll_x.config(command=self.criminal_table.xview)
        Scroll_y.config(command=self.criminal_table.yview)
        
        self.criminal_table.heading('1',text='caseid')
        self.criminal_table.heading('2',text='criminalnO') 
        self.criminal_table.heading('3',text='dateofcrime')
        self.criminal_table.heading('4',text='age') 
        self.criminal_table.heading('5',text='gender')
        self.criminal_table.heading('6',text='criminalname') 
        self.criminal_table.heading('7',text='status')
        self.criminal_table.heading('8',text='address')
        self.criminal_table.heading('9',text='crimetype')
        
        
        self.criminal_table['show']='headings'
        
        self.criminal_table.pack(fill=BOTH,expand=1)
        
        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.detch_data()
        
        
        
        #function declaration
        
    def add_data(self):
        if self.var_caseid.get()=="" or self.var_criminalname.get()=="" or self.var_criminalno.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="subh29-",database="details")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into crime values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                
                                                                                                  self.var_caseid.get(),
                                                                                                  self.var_criminalno.get(),
                                                                                                  self.var_dateofcrime.get(),
                                                                                                  self.var_age.get(),
                                                                                                  self.var_gender.get(),
                                                                                                  self.var_criminalname.get(),
                                                                                                  self.var_status.get(),
                                                                                                  self.var_address.get(),
                                                                                                  self.var_criminaltype.get()  
                                                                                       
                                                                                             
                                                                                             ))
                   
                        
        

                conn.commit()
                self.detch_data()
                self.clear_data                                                                                  
                conn.close()                                                                          
                messagebox.showinfo("success","criminal information saved successfully",parent=self.root)                                                                              
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)               

    #fetch data
   # def fetch_data
    def detch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="subh29-",database="details")
        my_cursor=conn.cursor()
        my_cursor.execute('select * from crime')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()        
                
        
     #get cursor
    def get_cursor(self,event=""):
        cursur_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursur_row)
        data=content['values']
        
        self.var_caseid.set(data[0])
        self.var_criminalno.set(data[1])
        self.var_dateofcrime.set(data[2])
        self.var_age.set(data[3])
        self.var_gender.set(data[4])
        self.var_criminalname.set(data[5])
        self.var_status.set(data[6])
        self.var_address.set(data[7])
        self.var_criminaltype.set(data[8]) 
          
    
    # update
    
    def update_data(self):
         if self.var_caseid.get()=="" or self.var_criminalname.get()=="" or self.var_criminalno.get()=="":
            messagebox.showerror("Error","All fields are required")
         else:
             try:
                 update=messagebox.askyesno('Update','Are You Sure To Update')
                 if update>0:
                      conn=mysql.connector.connect(host="localhost",username="root",password="subh29-",database="details")
                      my_cursor=conn.cursor()
                      my_cursor.execute('update crime set criminalno=%s,dateofcrime=%s,age=%s,gender=%s,criminalname=%s,status=%s,address=%s,criminaltype=%s where caseid=%s',(
                          
                                                                                                                                                                              
                                                                                                                                                                               self.var_criminalno.get(),
                                                                                                                                                                               self.var_dateofcrime.get(),
                                                                                                                                                                               self.var_age.get(),
                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                               self.var_criminalname.get(),
                                                                                                                                                                               self.var_status.get(),
                                                                                                                                                                               self.var_address.get(),
                                                                                                                                                                               self.var_criminaltype.get(),
                                                                                                                                                                               self.var_caseid.get(),            
                                                                                                                                                                            
                                                                                                                                                                            
                                                                                                                                                                             ))
            
                 else:
                    if not update:
                        return
                 conn.commit()
                 self.detch_data()
                 self.clear_data()
                 conn.close()
                 messagebox.showerror('success','criminal record has been updated')          
             except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')
                
                
    #delete
    def delete_data(self):
        if self.var_caseid.get()=="" or self.var_criminalname.get()=="" or self.var_criminalname.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                 Delete=messagebox.askyesno('Delete','Are You Sure To Delete')
                 if Delete>0:
                     conn=mysql.connector.connect(host="localhost",username="root",password="subh29-",database="details")
                     my_cursor=conn.cursor()
                     sql='delete from crime where caseid=%s'
                     value=(self.var_caseid.get(),)
                     my_cursor.execute(sql,value)
                 else:
                     if not Delete:
                         return
                 conn.commit()
                 self.detch_data()
                 self.clear_data()
                 conn.close()
                 messagebox.showerror('success','criminal record has been deleted')          
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')        
         #clear
    def clear_data(self):
        self.var_caseid.set("")
        self.var_criminalno.set("")
        self.var_dateofcrime.set("")
        self.var_age.set("")
        self.var_gender.set("")
        self.var_criminalname.set("")
        self.var_status.set("")
        self.var_address.set("")
        self.var_criminaltype.set("")             
        
        
        #search
    def serch_data(self):
            if self.var_com_search.get()=="":
                messagebox.showerror('Error','All fields are required')
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="subh29-",database="details")
                    my_cursor=conn.cursor()
                    my_cursor.execute('select * from crime where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                    rows=my_cursor.fetchall()
                    if len(rows)!=0:
                        self.criminal_table.delete(*self.criminal_table.get_children())
                        for i in rows:
                            self.criminal_table.insert('',END,values=i)
                    conn.commit()
                    conn.close() 
                except Exception as es:
                    messagebox.showerror('Error',f'Due To{str(es)}')
                    
                    
                    
                    #generate criminal data set
                            
        
    def generate_dataset(self):
            if self.var_caseid.get()=="" or self.var_criminalname.get()=="" or self.var_caseid.get()=="":
             messagebox.showerror("Error","All fields are required")
            else:
                try:   
                    conn=mysql.connector.connect(host="localhost",username="root",password="subh29-",database="details")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from crime")
                    crimeresult=my_cursor.fetchall()
                    id=0
                    for  x in crimeresult:
                         id+=1
                    my_cursor.execute('update crime set criminalno=%s,dateofcrime=%s,age=%s,gender=%s,criminalname=%s,status=%s,address=%s,criminaltype=%s where caseid=%s',(
                          
                                                                                                                                                                              
                                                                                                                                                                               self.var_criminalno.get(),
                                                                                                                                                                               self.var_dateofcrime.get(),
                                                                                                                                                                               self.var_age.get(),
                                                                                                                                                                               self.var_gender.get(),
                                                                                                                                                                               self.var_criminalname.get(),
                                                                                                                                                                               self.var_status.get(),
                                                                                                                                                                               self.var_address.get(),
                                                                                                                                                                               self.var_criminaltype.get(),
                                                                                                                                                                               self.var_caseid.get()==id+1           
                                                                                                                                                                            
                                                                                                                                                                            
                
                                                                                                                                                                 ))            
                    conn.commit()
                    self.detch_data()
                    self.clear_data()
                    conn.close()
                
                #load predifiend data on face frontal from open cv 
                
                
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
                
                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                    
                    
                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
        
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(548,250))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("cropped Face",face)
        
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("captured","Image captured successfully")
                except Exception as es:
                    messagebox.showerror('Error',f'Due To{str(es)}') 
                    
    
    #train image
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        
        for image in path:
            img=Image.open(image).convert('L')    #gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.'[1]))
            
            
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
    obj=Criminal(root)
    root.mainloop()                   
           

        
