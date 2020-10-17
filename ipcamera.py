import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os,numpy
import datetime
from intro import intro

intro()

logo = cv2.imread("logo.png")
safe = cv2.imread("safe.png")
stop = cv2.imread("stop.png")
stream = cv2.VideoCapture(0)  

while True:
    r, f = stream.read()
    small_frame = cv2.resize(f, (0, 0), fx=0.25, fy=0.25)
    origin = cv2.resize(f, (0, 0), fx=0.7, fy=0.7)
    mil = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(mil)

    if len(face_locations)==0:
        print("Safe to drive, No one detected!")
        status = numpy.array(safe)
    else:
        status = numpy.array(stop)

    for x1,y1,x2,y2 in face_locations:
        a1 = max(x1,x2)*4
        b1 = max(y1,y2)*4
        a2 = min(x1,x2)*4
        b2 = min(y1,y2)*4  
        cv2.rectangle(f, (b2, a2),( b1, a1), (0, 255, 0), 5)
        font = cv2.FONT_HERSHEY_DUPLEX
        print("Human Detected @", (x1,y1,x2,y2), datetime.datetime.now())
        cv2.putText(f, "Human", ( b2, a1+28), font, 1.0, (0, 255, 0), 1)

    #watermark
    watermark = Image.open('logo.png')
    pil = Image.fromarray(numpy.uint8(f)).convert('RGB')
    pil.paste(watermark, (0, 0), watermark)
    open_cv_image = numpy.array(pil)
    f = open_cv_image[:, :, ::-1].copy()
    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
    # Custom window
    title = 'Powered by Adaptive AgroTech. 2020'
    cv2.namedWindow(title, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(title, f)
    cv2.resizeWindow(title, 800, 600)
    cv2.moveWindow(title, 1000, 50)

    # Depth view
    g = cv2.cvtColor(origin, cv2.COLOR_BGR2HLS_FULL)
    cv2.imshow("Depth View", g)

    # Status Window
    cv2.imshow("Status", status)
    cv2.moveWindow("Status", 1000,800)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()