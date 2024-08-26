import cv2
import numpy as np
import mediapipe as mp
import time
#cvtocvzone
import cvzone
from cvzone.HandTrackingModule import HandDetector
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()  # This returns a tuple: (minVolume, maxVolume, somethingElse)
minVolume = volRange[0]
maxVolume = volRange[1]






cap = cv2.VideoCapture(0)

detector = HandDetector(detectionCon=0.8, maxHands=1,minTrackCon=0.8)
ptime = 0
while True:
    success, img = cap.read()
    hands, bboxInfo = detector.findHands(img,draw=True)
    if len(hands) != 0:

        lsList = hands[0]['lmList']
        x1,y1 = lsList[4][0], lsList[4][1]
        x2,y2 = lsList[8][0], lsList[8][1]
        # # print(hand[4], hand[8])
        # cv2.circle(img, (hand[4][0], hand[4][1]), 10, (255, 0, 255), cv2.FILLED)
        # cv2.circle(img, (hand[8][0], hand[8][1]), 10, (255, 0, 255), cv2.FILLED)
        # cv2.line(img, (hand[4][0], hand[4][1]), (hand[8][0], hand[8][1]), (255, 0, 255), 2)

        # cx,cy=(hand[4][0]+hand[8][0])//2,(hand[4][1]+hand[8][1])//2
        # cv2.circle(img, (cx,cy), 10, (255, 0, 255), cv2.FILLED)

    
        length,_,img= detector.findDistance((x1,y1),(x2,y2),img)
        # print(length)
        minLength = 16
        maxLength = 85
        volumeLevel = np.interp(length, [minLength, maxLength], [minVolume, maxVolume])
        volumePer = np.interp(length, [minLength, maxLength], [0, 100])
        volumeBar = np.interp(length, [minLength, maxLength], [400, 150])
        

        volume.SetMasterVolumeLevel(volumeLevel, None)

        cv2.putText(img, f'Volume: {int(volumePer),'%'}', (400, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

        cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv2.rectangle(img, (50, int(volumeBar)), (85, 400), (255, 0, 0), cv2.FILLED)




    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f"FPS:{int(fps)} ", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    