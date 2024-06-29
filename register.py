import face_recognition
import cv2
import numpy as np
import sqlite3

name = input("Enter the name: ")

video_capture = cv2.VideoCapture(0);
ret, frame = video_capture.read()
small_frame=cv2.resize(frame, (0,0),fx=0.25,fy=0.25)
rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

face_locations = face_recognition.face_locations(rgb_small_frame)
face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)

video_capture.release()
cv2.destroyAllWindows()

encodings_to_insert = []

for i in face_encodings:
    encoding_str = ','.join(map(str, i))
    encodings_to_insert.append(encoding_str)


with sqlite3.connect("database.db") as con:
    cur = con.cursor()
    for encoding_str in encodings_to_insert:
        cur.execute("INSERT INTO faces(name, encoding) VALUES(?, ?)", (name, encoding_str))
    con.commit()


if (cur.rowcount>0):
    print("Encoding saved successfully")
else:
    print("Failed to save encoding check lighting conditions")