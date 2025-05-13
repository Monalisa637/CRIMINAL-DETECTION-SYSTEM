from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from criminal import Criminal
import os
import cv2
import mysql.connector
import numpy as np
from tkinter import messagebox
import requests
import smtplib


class facerecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("530x530+800+140")
        self.root.title("FACE IDENTIFICATION")

        img6 = Image.open("IMAGES/button1.png")
        img6 = img6.resize((520, 80), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(self.root, image=self.photoimg6, cursor="hand2", command=self.face_recog)
        b6.place(x=0, y=465, width=528, height=60)

        b_6 = Button(b6, text="FACE DETECTOR", command=self.face_recog, cursor="hand2", font=('times new roman', 16, 'bold'), bg='white', fg='black')
        b_6.place(x=125, y=7, width=300, height=40)

    def get_location(self):
        try:
            response = requests.get("https://ipinfo.io/")
            data = response.json()
            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]
            return f"Latitude: {latitude}, Longitude: {longitude}"
        except:
            return "Failed to fetch location data"

    def send_email(self):
        sender_email = "das.sontoskumar@gmail.com"
        sender_password = "Dipu2022*"
        recipient_email = "raymonalisa77@gmail.com"

        # Create the email message
        subject = "Criminal Identified"
        body = "A criminal has been identified."
        message = f"Subject: {subject}\n\n{body}"

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message)
            print("Email sent successfully")

        except Exception as e:
            print("An error occurred while sending the email:", str(e))

        finally:
            # Disconnect from the server
            server.quit()

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="subh29-", database="details")
                my_cursor = conn.cursor()

                my_cursor.execute("select criminalname from crime where caseid=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute("select criminalno from crime where caseid=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                if confidence > 77:
                    cv2.putText(img, f"CriminalNo: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {i}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.send_email()
                    
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Not Identified", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    
                
                latitude_longitude = self.get_location()
                if latitude_longitude != "Failed to fetch location data":
                    latitude, longitude = latitude_longitude.split(",")
                    print("Latitude:", latitude)
                    print("Longitude:", longitude)
                    
                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 55, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Criminal Identification", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = facerecognition(root)
    root.mainloop()
