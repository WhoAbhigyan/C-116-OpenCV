import cv2
img=cv2.imread("C:/Users/hp/Dropbox/My PC (ROG)/Desktop/C-116/PRO-c116-OpenCV-Image-Assets-main/poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
text_to_show="Hello"
cv2.putText(img,text_to_show,(100,200),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,120,0))
cv2.imshow("output",img)
cv2.waitKey(0)