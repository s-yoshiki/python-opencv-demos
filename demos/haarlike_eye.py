#coding:utf-8
import cv2
import cv2.cv as cv
import numpy as num


cascade_folder = "/usr/local/opt/opencv/share/OpenCV/haarcascades/"

#cascade_path = "haarcascade_eye.xml"
cascade_path = "haarcascade_eye_tree_eyeglasses.xml"
#cascade_path = "haarcascade_frontalcatface.xml"
#cascade_path = "haarcascade_frontalcatface_extended.xml"
#cascade_path = "haarcascade_frontalface_alt.xml"
#cascade_path = "haarcascade_frontalface_alt2.xml"
#cascade_path = "haarcascade_frontalface_alt_tree.xml"
#cascade_path = "haarcascade_frontalface_default.xml"
#cascade_path = "haarcascade_fullbody.xml"
#cascade_path = "haarcascade_lefteye_2splits.xml"
#cascade_path = "haarcascade_licence_plate_rus_16stages.xml"
#cascade_path = "haarcascade_lowerbody.xml"
#cascade_path = "haarcascade_mcs_eyepair_big.xml"
#cascade_path = "haarcascade_mcs_eyepair_small.xml"
#cascade_path = "haarcascade_mcs_leftear.xml"
#cascade_path = "haarcascade_mcs_lefteye.xml"
#cascade_path = "haarcascade_mcs_mouth.xml"
#cascade_path = "haarcascade_mcs_nose.xml"
#cascade_path = "haarcascade_mcs_rightear.xml"
#cascade_path = "haarcascade_mcs_righteye.xml"
#cascade_path = "haarcascade_mcs_upperbody.xml"
#cascade_path = "haarcascade_profileface.xml"
#cascade_path = "haarcascade_righteye_2splits.xml"
#cascade_path = "haarcascade_russian_plate_number.xml"
#cascade_path = "haarcascade_smile.xml"
#cascade_path = "haarcascade_upperbody.xml"


cascade = cv2.CascadeClassifier(cascade_folder+cascade_path)

def capture_camera(mirror=True, size=None):
    try:
        cap = cv2.VideoCapture(0)
    except:
        print "camera was not found"

    cv2.namedWindow('camera capture')
    color = (0, 200, 2)
    while True:
        try:
            ret,frame = cap.read()
            frame2 = frame.copy()
            #frame2 = frame
        except:
            cap = cv2.VideoCapture(1)
            ret,frame = cap.read()
            frame2 = frame.copy()
        

        
        if len(frame.shape) == 3:
            height, width, channels = frame.shape[:3]
        else:
            height, width = frame.shape[:2]
            channels = 1

        
        if mirror is True:
            frame = frame[:,::-1]
            frame = cv2.flip(frame,1)

        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(65, 65))
        #print facerect

        if len(facerect) > 0:
            for rect in facerect:
                #print "success"
                x1 = rect[1]
                y1 = rect[0]
                w1 = rect[3]
                h1 = rect[2]
                #eye = frame[x1:x1+w1,y1:y1+h1]
                #eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)

                try:
                    cv2.rectangle(frame2, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=5)
                except:
                    print("Could not try 'cv2.rectangle'")



        cv2.imshow('camera capture', frame2)
        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_camera(False)
