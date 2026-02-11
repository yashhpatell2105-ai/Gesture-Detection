import cv2

face_cascade = cv2.CascadeClassifier("Programes\Python\Python5-OpenCV\Haarcascade\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)

    """
    1.1 = zoom slowly to detect face with garuri background
    5 = minnegbour ,to check 5 diffrent angle to check its a real face
    """
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    """
    face = [
    (100,150,80,60) face1
    (250,120,80,90) face2
    ]    
    x - how far from left
    y - how far from top
    w - width of face
    h - height of face
    """

    cv2.imshow("Web cam face detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()