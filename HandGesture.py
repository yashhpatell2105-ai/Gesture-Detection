from cvzone.HandTrackingModule import HandDetector
import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)


# Create a blank image (black background)


# Previous position (for drawing a line)

cv2.namedWindow("Air Drawing", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Air Drawing", 640, 480)



while True:
    success, img = cap.read()
    # Flip image so it acts like a mirror
    img = cv2.flip(img,1)

    # Detect the hand
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]  # List of all 21 landmark points
        fingers = detector.fingersUp(hand1)

        # Thumb up gesture (thumb = 1, rest = 0)
        if   fingers == [1, 0, 0, 0, 0]:
            cv2.putText(img,"Thumb is up!", (100,100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)
  
        elif fingers == [0, 1, 1, 0, 0]:         
            cv2.putText(img,"index and middle fingure is up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)
   
        elif fingers == [0, 0, 1, 0, 0]:         
            cv2.putText(img,"Not This", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 2)
    
        elif fingers == [0, 1, 0, 0, 0]:          
            cv2.putText(img,"Index fingure is up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)

        elif fingers == [0, 0, 0, 1, 0]:           
            cv2.putText(img,"ring fingure is up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)

        elif fingers == [0, 0, 0, 0, 1]:            
            cv2.putText(img,"pinky is up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)

        elif fingers == [0, 0, 0, 0, 0]:            
            cv2.putText(img,"all fingure are down!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)

        elif fingers == [1, 1, 1, 1, 1]:            
            cv2.putText(img,"all fingure are up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)
        
        elif fingers == [1, 0, 0, 0, 1]:            
            cv2.putText(img,"thumb and pinky us up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)

        elif fingers == [0, 1, 1, 1, 1]:            
            cv2.putText(img,"first four fingure are up!", (100, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,255), 2)
            
        elif fingers == [0, 1, 1, 1, 0]:
            cv2.putText(img,"first three fingers are up",(100,100),cv2.FONT_HERSHEY_DUPLEX, 1,(0,255,225),2)



        else:
            x1, y1 = 0, 0

    # Combine original image and drawing canvas
  

    # Show the images
    
    cv2.imshow("Air Drawing", img)
    
    

    # Exit when 'q' pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
