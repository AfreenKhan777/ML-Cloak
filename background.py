import cv2#CV is computer vision.Open CV is a library of python for image & video processing
# THIS IS MY WEBCAM
cap = cv2.VideoCapture(0)#0 is the link of webcam

while cap.isOpened():#true
    
    #ret is return
    #back is a word(any word of your choice except keywords) that tells what camerais reading(here for background image)
    #cap is video capture
    #read returns 2 values read & return
    ret, back = cap.read() #HERE I AM SIMPLY READING FROM MY WEBCAM
    if ret:
        #if we are getting something in back
        cv2.imshow("image", back)
        #to break
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
