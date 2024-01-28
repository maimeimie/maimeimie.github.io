import cv2
import face_recognition
import numpy as np
from tkinter import*
import tkinter as tk
from datetime import datetime
import csv
from PIL import Image,ImageTk

personl_name = "Narathip"
person_image = face_recognition.load_image_file("./helloeveryone1-main/photos/cee.jpg")
persponl_face_encoding = face_recognition.face_encodings(person_image)[0]

personl2_name = "Thanatorn"
person2_image = face_recognition.load_image_file("./helloeveryone1-main/photos/bank.jpg")
persponl2_face_encoding = face_recognition.face_encodings(person2_image)[0]

personl3_name = "Tharakorn"
personl3_image = face_recognition.load_image_file("./helloeveryone1-main/photos/jino.jpg")
persponl3_face_encoding  = face_recognition.face_encodings(personl3_image)[0]

personl4_name = "Punya"
personl4_image = face_recognition.load_image_file("./helloeveryone1-main/photos/kao.jpg")
persponl4_face_encoding = face_recognition.face_encodings(personl4_image)[0]

personl5_name = "Nakrop"
personl5_image = face_recognition.load_image_file("./helloeveryone1-main/photos/nakrop.jpg")
persponl5_face_encoding = face_recognition.face_encodings(personl5_image)[0]

personl6_name = "Panita"
personl6_image = face_recognition.load_image_file("./helloeveryone1-main/photos/Pan.jpg")
persponl6_face_encoding = face_recognition.face_encodings(personl6_image)[0]

personl7_name = "Thawanporn"
personl7_image = face_recognition.load_image_file("./helloeveryone1-main/photos/susi.jpg")
persponl7_face_encoding = face_recognition.face_encodings(personl7_image)[0]

personl8_name = "Chayanan"
personl8_image = face_recognition.load_image_file("./helloeveryone1-main/photos/pinky.jpg")
persponl8_face_encoding = face_recognition.face_encodings(personl8_image)[0]

personl9_name = "Phitaphorn"
personl9_image = face_recognition.load_image_file("./helloeveryone1-main/photos/mint.jpg")
persponl9_face_encoding = face_recognition.face_encodings(personl9_image)[0]

personl10_name = "Natchanan"
personl10_image = face_recognition.load_image_file("./helloeveryone1-main/photos/bew.jpg")
persponl10_face_encoding = face_recognition.face_encodings(personl10_image)[0]

personl11_name = "Paison"
personl11_image = face_recognition.load_image_file("./helloeveryone1-main/photos/ingk 1.jpg")
persponl11_face_encoding = face_recognition.face_encodings(personl11_image)[0]

personl12_name = "Paudda"
personl12_image = face_recognition.load_image_file("./helloeveryone1-main/photos/ingk 2.jpg")
persponl12_face_encoding = face_recognition.face_encodings(personl12_image)[0]

personl13_name = "Sirikanya"
personl13_image = face_recognition.load_image_file("./helloeveryone1-main/photos/Jaja.jpg")
persponl13_face_encoding = face_recognition.face_encodings(personl13_image)[0]

personl14_name = "Sunisa"
personl14_image = face_recognition.load_image_file("./helloeveryone1-main/photos/Cherry.jpg")
persponl14_face_encoding = face_recognition.face_encodings(personl14_image)[0]

personl15_name = "Rawiwan"
personl15_image = face_recognition.load_image_file("./helloeveryone1-main/photos/Kuk.jpg")
persponl15_face_encoding = face_recognition.face_encodings(personl15_image)[0]

personl16_name = "Rachan"
personl16_image = face_recognition.load_image_file("./helloeveryone1-main/photos/plng.jpg")
persponl16_face_encoding = face_recognition.face_encodings(personl16_image)[0]

personl17_name = "Sasipapa"
personl17_image = face_recognition.load_image_file("./helloeveryone1-main/photos/Soda.jpg")
persponl17_face_encoding = face_recognition.face_encodings(personl17_image)[0]

personl18_name = "Sirinan"
personl18_image = face_recognition.load_image_file("./helloeveryone1-main/photos/pleng.jpg")
persponl18_face_encoding = face_recognition.face_encodings(personl18_image)[0]

personl19_name = "Manutchaya"
personl19_image = face_recognition.load_image_file("./helloeveryone1-main/photos/beam.jpg")
persponl19_face_encoding = face_recognition.face_encodings(personl19_image)[0]

personl20_name = "Tnatcha"
personl20_image = face_recognition.load_image_file("./helloeveryone1-main/photos/Oon.jpg")
persponl20_face_encoding = face_recognition.face_encodings(personl20_image)[0]


known_face_encodings = [
    persponl_face_encoding,
    persponl2_face_encoding,
    persponl3_face_encoding,
    persponl4_face_encoding,
    persponl5_face_encoding,
    persponl6_face_encoding,
    persponl7_face_encoding,
    persponl8_face_encoding,
    persponl9_face_encoding,
    persponl10_face_encoding,
    persponl11_face_encoding,
    persponl12_face_encoding,
    persponl13_face_encoding,
    persponl14_face_encoding,
    persponl15_face_encoding,
    persponl16_face_encoding,
    persponl17_face_encoding,
    persponl18_face_encoding,
    persponl19_face_encoding,
    persponl20_face_encoding
]


known_face_names = [
personl_name,
personl2_name,
personl3_name,
personl4_name,
personl5_name,
personl6_name,
personl7_name,
personl8_name,
personl9_name,
personl10_name,
personl11_name,
personl12_name,
personl13_name,
personl14_name,
personl15_name,
personl16_name,
personl17_name,
personl18_name,
personl19_name,
personl20_name
]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(current_date+ '.csv', 'w+', newline ='')
exwriter = csv.writer(f)

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")
        self.root.title("Face Recognition System")

        colur = "gray17"

        main_frame = tk.Frame(root, bg=colur, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        self.canvas = Canvas(self.root, width=0, height=0)
        self.canvas.pack()

        b1 = Button(
            main_frame,
            text="start",
            width=20,
            height=3,
            cursor="hand2",
            border=0,
            font=('Arial', 15, 'bold'),
            command=self.switch_page
        )
        b1.grid(column=0, row=0)

    def switch_page(self):
        self.root.withdraw()

        self.new_window = Tk()
        self.new_window.geometry("1600x900+0+0")
        self.new_window.title("Face Denition")

        colur = "gray17"
        canvas = tk.Canvas(self.new_window, width=1600, height=900, bg=colur)
        
        back_button = Button(
            self.new_window, 
            text="Back to Main",
            width=10,
            height=5, 
            border=0,
            cursor="hand2",
            font=('Arial', 15, 'bold'),
            command=self.back_to_main)
        
        back_button.grid(column=0, row=0)
        back_button.pack()
        canvas.pack()
        

        self.show_webcam()

    def show_webcam(self):
        cv2.namedWindow("Face Detection", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Face Detection", 1600, 900)
      
   
        cap = cv2.VideoCapture(1)

        cap.set(4, 640)
        cap.set(3, 480)

        imgBg = cv2.imread('./helloeveryone1-main/pictures/White2.jpg')
        

        while True:
          ret, img = cap.read()
          if not ret:
                print("Failed to grab frame from the webcam")
                break
          img_resized = cv2.resize(img, (640, 480))
          bg_height, bg_width, _ = imgBg.shape
          img_height, img_width, _ = img_resized.shape

          start_y = (bg_height - img_height) // 2
          end_y = start_y + img_height
          start_x = (bg_width - img_width) // 2
          end_x = start_x + img_width
          imgBg[start_y:end_y, start_x:end_x] = img_resized
          resize_frame = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
          rgb_resize_frame = resize_frame[:,:,::-1]
          if s:
                face_locations = face_recognition.face_locations(rgb_resize_frame, number_of_times_to_upsample=2)
                face_encodings = face_recognition.face_encodings(rgb_resize_frame, face_locations, num_jitters=5)
                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
                    name =''
                    face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
                    best_match_index = np.argmin(face_distance)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                        face_names.append(name)
                        if name in known_face_names:
                            if name in students:
                             students.remove(name)
                             print(students)
                             current_time = now.strftime("%H-%M-%S")
                             exwriter.writerow([name, current_time])
                             
          cv2.imshow("Face Detection", imgBg)
          if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()  
        cv2.destroyAllWindows()
        f.close()
        
    def back_to_main(self):
         self.new_window.destroy()
         self.root.deiconify()

if __name__ == "__main__":
   root = Tk()
   obj = FaceRecognitionSystem(root)
   root.mainloop()
    