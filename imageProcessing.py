import cv2 
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("cannot open camera")
    exit()
while True:
    ret,frame = cap.read()
    if not ret:
        print("cannot recieve frame")
        break
    cv2.imshow("camera",frame)
    if cv2.waitKey(1)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()