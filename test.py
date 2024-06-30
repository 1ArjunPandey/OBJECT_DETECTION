import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone

# print("hello")
model=YOLO('best.pt')
cy1 = 311
offset = 6
pack = []

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

cap=cv2.VideoCapture('cy.mp4')


my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n") 
#print(class_list)

count=0
tracker=Tracker()

while True:    
    ret,frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,500))
   

    results=model.predict(frame)
 #   print(results)
    a=results[0].boxes.data
    px=pd.DataFrame(a).astype("float")
#    print(px)
    list=[]
             
    for index,row in px.iterrows():
#        print(row)
 
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]

        list.append([x1,y1,x2,y2])

    bbox_idx=tracker.update(list)

    for bbox in bbox_idx:
        x3,y3,x4,y4,id=bbox
        cx=int(x3+x4)//2
        cy=int(y3+y4)//2
        if cy1 < (cy + offset) and cy1 > (cy-offset):

            cv2.circle(frame,(cx,cy),4,(255,0,0),-1)
            cv2.rectangle(frame,(x3,y3),(x4,y4),(0, 255, 30),2)
            cvzone.putTextRect(frame,f'package',(x3,y3),1,1)
            if pack.count(id) == 0:
                pack.append(id)

    cntt = (len(pack))
    cv2.line(frame, (259, cy1), (547, cy1), (255, 255, 255), 2)
    cvzone.putTextRect(frame,f'total : {cntt}',(50, 60), 2,1)
    cv2.imshow("RGB", frame)

    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
