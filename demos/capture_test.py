#coding:utf-8
import cv2
color = (0, 2, 2)
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()

        if mirror is True:
            frame = frame[:,::-1]

        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        #cv2.rectangle(frame, (10,10),(50,50),color, cv2.cv.CV_FILLED)
        cv2.imshow('camera capture', frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()

    cv2.destroyAllWindows()

capture_camera()
