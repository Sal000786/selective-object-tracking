import cv2
import imutils
TrDict = {
    'csrt': cv2.TrackerCSRT_create,
         'kcf' : cv2.TrackerKCF_create,
        }

tracker = TrDict['kcf']()
v = cv2.VideoCapture("C:/Users/salma/Downloads/crowd_video.mp4") # video
# v = cv2.VideoCapture("F:\\sample_project\\venv\\Scripts\\test_video.mp4")
ret, frame = v.read()
frame = imutils.resize(frame,width=600)
cv2.imshow('Frame',frame)
bb = cv2.selectROI('Frame',frame)
tracker.init(frame,bb)
while True:
    ret, frame = v.read()
    if not ret:
        break
    frame = imutils.resize(frame,width=600)
    (success,box) = tracker.update(frame)
    if success:
        (x,y,w,h) = [int(a) for a in box]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(100,255,0),2)
    cv2.imshow('Frame',frame)
    key = cv2.waitKey(5) & 0xFF
    if key == ord('q'):
        break
v.release()
cv2.destroyAllWindows()
        
    
    