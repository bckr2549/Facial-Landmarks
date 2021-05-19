import cv2
import mediapipe as mp

#face mash
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
#Image
img = cv2.imread("photoes/chenna.jpeg")
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
        cv2.circle(img, (x,y), 2, (255,255,0),-1)
        #cv2.putText(img, str(i),(x,y),0,1,(0,0,0))
cv2.imshow("chenna", img)
#cv2.imshow("chenna", rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()