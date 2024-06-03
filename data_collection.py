import cv2
from cvzone.FaceDetectionModule import FaceDetector
import cvzone
from time import time
import os

###########################################
classId = 1  # 0 for fake and 1 for real
outputFolderPath = 'Dataset/DataCollect'
confidence = 0.8
save = True
blurThreshold = 35  # larger is more focus

debug = False
offsetPercentageW = 10
offsetPercentageH = 20
camWidth, camHeight = 640, 480
floatingPoint = 6
#########################################

cap = cv2.VideoCapture(0)
cap.set(3, camWidth)
cap.set(4, camHeight)
detector = FaceDetector()

while True:
    success, img = cap.read()

    imgOut = img.copy()
    if not success:
        print("Failed to read the frame.")
        break

    img, bboxs = detector.findFaces(img, draw=False)

    listBlur = []  # True False Value indicating if the faces are blur or not
    listInfo = []  # normalized values and the class
    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        for bbox in bboxs:
            x, y, w, h = bbox['bbox']
            score = bbox['score'][0]

            # ---------------- Check the score  -----------
            if score > confidence:
                offsetW = (offsetPercentageW / 100) * w

                x = int(x - offsetW)
                w = int(w + offsetW * 2)

                offsetH = (offsetPercentageH / 100) * h

                y = int(y - offsetH * 3)
                h = int(h + offsetH * 3.5)

                # ---------- To avoid Values below 0---------
                x = max(0, x)
                y = max(0, y)
                w = max(0, w)
                h = max(0, h)

                # ------------ Find Blurriness ------------
                imgFace = img[y:y + h, x:x + w]
                blurredValue = int(cv2.Laplacian(imgFace, cv2.CV_64F).var())
                if blurredValue > blurThreshold:
                    listBlur.append(True)
                else:
                    listBlur.append(False)

                # ------- Normalize values -------
                ih, iw, _ = img.shape
                xc, yc = x + w / 2, y + h / 2
                xcn, ycn = round(xc / iw, floatingPoint), round(yc / ih, floatingPoint)
                wn, hn = round(w / iw, floatingPoint), round(h / ih, floatingPoint)

                # ---------- To avoid Values above 1---------
                xcn = min(1, xcn)
                ycn = min(1, ycn)
                wn = min(1, wn)
                hn = min(1, hn)

                listInfo.append(f"{classId} {xcn} {ycn} {wn} {hn}\n") # reuired by yolo

                # ------Drawing -----------
                cv2.rectangle(imgOut, (x, y, w, h), (255, 0, 0), 3)
                cvzone.putTextRect(imgOut, f'Score:{int(score * 100)}%, Blur:{blurredValue}', (x, y - 20),
                                   scale=1, thickness=2)
                if debug:
                    cv2.rectangle(img, (x, y, w, h), (255, 0, 0), 3)
                    cvzone.putTextRect(img, f'Score:{int(score * 100)}%, Blur:{blurredValue}', (x, y - 20),
                                       scale=1, thickness=2)

        # ---------To save ------------
        if save:
            if all(listBlur) and listBlur:
                # -----------Save image -----
                if not os.path.exists(outputFolderPath):
                    os.makedirs(outputFolderPath)
                timeNow = str(time()).replace(".", "")
                print(f"Saving image at: {outputFolderPath}/{timeNow}.jpg")
                cv2.imwrite(f"{outputFolderPath}/{timeNow}.jpg", img)

                # -----------Save Label Text File -----
                for info in listInfo:
                    f = open(f"{outputFolderPath}/{timeNow}.txt", 'a')
                    f.write(info)
                    f.close()



    cv2.imshow("Image", imgOut)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
