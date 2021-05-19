import cv2
import mediapipe as mp

#face mash
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    #Image
    ret, img = cap.read()
    if ret is not True:
        break
    # img = cv2.imread("photoes/chenna.jpeg")
    height, width,_ = img.shape
    print("Height, width", height, width)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Facial landmarks
    result = face_mesh.process(rgb_img)

    for facial_landmarks in result.multi_face_landmarks:
         for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            x = int(pt1.x * width)
            y = int(pt1.y * height)
            cv2.circle(img, (x,y), 2, (250,0,0),-1)
        #cv2.putText(img, str(i),(x,y),0,1,(0,0,0))
    cv2.imshow("lady", img)
#cv2.imshow("lady", rgb_img)
    cv2.waitKey(30)
    cv2.destroyAllWindows()