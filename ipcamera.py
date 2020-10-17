"""Access IP Camera in Python OpenCV"""

import cv2
import face_recognition
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import os,numpy
import datetime

logo = cv2.imread("logo.png")
stream = cv2.VideoCapture(0)  

while True:
    r, f = stream.read()
    small_frame = cv2.resize(f, (0, 0), fx=0.25, fy=0.25)
    mil = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(mil)
    if len(face_locations)==0:
        print("NO ONE !")

    for x1,y1,x2,y2 in face_locations:
        a1 = max(x1,x2)*4
        b1 = max(y1,y2)*4
        a2 = min(x1,x2)*4
        b2 = min(y1,y2)*4  
        cv2.rectangle(f, (b2, a2),( b1, a1), (0, 255, 0), 5)
        font = cv2.FONT_HERSHEY_DUPLEX
        print("PEYMAN Detected @", (x1,y1,x2,y2), datetime.datetime.now())
        cv2.putText(f, "Face", ( b2, a1+28), font, 1.0, (0, 255, 0), 1)


        
    # # Write some Text

    # font                   = cv2.FONT_HERSHEY_DUPLEX
    # bottomLeftCornerOfText = (10,20)
    # fontScale              = 0.5
    # fontColor              = (0,0,0)
    # lineType               = 1

    # cv2.putText(f,"SunBot, Human-Aware Navigation", 
    #     bottomLeftCornerOfText, 
    #     font, 
    #     fontScale,
    #     fontColor,
    #     lineType)
        

    # # Write some Text

    # font                   = cv2.FONT_HERSHEY_DUPLEX
    # bottomLeftCornerOfText = (10,30)
    # fontScale              = 0.3
    # fontColor              = (0,0,0)
    # lineType               = 1

    # cv2.putText(f,"Powered by Adaptive AgroTech. 2020", 
    #     bottomLeftCornerOfText, 
    #     font, 
    #     fontScale,
    #     fontColor,
    #     lineType)
        

    #f[0:logo.shape[0], 0:logo.shape[1]] = logo
    #cv2.imshow('IP Camera stream',f)

    watermark = Image.open('logo.png')
    PIL_image = Image.fromarray(numpy.uint8(f)).convert('RGB')

    PIL_image.paste(watermark, (0, 0), watermark)

    open_cv_image = numpy.array(PIL_image) 
    # Convert RGB to BGR 
    f = open_cv_image[:, :, ::-1].copy() 

    f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)



    # Custom window
    title = 'Powered by Adaptive AgroTech. 2020'
    cv2.namedWindow(title, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(title, f)
    cv2.resizeWindow(title, 1000, 750)

        


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()