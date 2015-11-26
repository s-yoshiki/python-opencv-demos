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

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        thrs1 =1000
        thrs2 =10
        edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)

        cv2.imshow('camera capture', edge)
        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()

    cv2.destroyAllWindows()

capture_camera()
