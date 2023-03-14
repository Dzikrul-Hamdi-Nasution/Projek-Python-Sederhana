import numpy as np
import cv2
  
Known_distance = 7.2 
Known_width = 10.3
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
fonts = cv2.FONT_HERSHEY_COMPLEX

webcam = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
  
def Focal_Length_Finder(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image * measured_distance) / real_width
    return focal_length

def Distance_finder(Focal_Length, real_face_width, face_width_in_frame):
    distance = (real_face_width * Focal_Length)/face_width_in_frame
    return distance



def face_data(imageFrame):
    
    face_width = 0  
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([0, 141, 215], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)   
    
    kernal = np.ones((5, 5), "uint8")
      
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = blue_mask)
   
    contours, hierarchy = cv2.findContours(blue_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)


    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 500):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 255), 2)
            face_width = w
              
            cv2.putText(imageFrame, "Ball", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255,255, 255))



    
   
    return face_width





ref_image = cv2.imread("sampel.jpg")

ref_image_face_width = face_data(ref_image)

Focal_length_found = Focal_Length_Finder(
    Known_distance, Known_width, ref_image_face_width)

cv2.imshow("ref_image", ref_image)



while(1):
      

    _, imageFrame = webcam.read()


    face_width_in_frame = face_data(imageFrame)

    if face_width_in_frame != 0:
    
        Distance = Distance_finder(
            Focal_length_found, Known_width, face_width_in_frame)
 
        # draw line as background of text
        cv2.line(imageFrame, (30, 30), (230, 30), RED, 32)
        cv2.line(imageFrame, (30, 30), (230, 30), BLACK, 28)
 
        # Drawing Text on the screen
        cv2.putText(
            imageFrame, f"Distance: {round(Distance,2)} CM", (30, 35),
          fonts, 0.6, GREEN, 2)








    
    

              
    cv2.imshow("Deteksi Bola", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break