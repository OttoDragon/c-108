import cv2
import mediapipe as mp

finger_tips =[8, 12, 16, 20]



for tip in finger_tips:
    x, y = int(lm_list[tip]).x*w), inst(lm_list[tip].y*h)
    cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED)

if lm_list[tip].x < lm_list[tip - 3].x:
    v2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
    finger_fold_status.append(True)
else:
    finger_fold_status.append(False)

if all(finger_fold_status):
    if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y:
        print("CURTI")
        cv2.putText(img, "CURTI", (20, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

    if lm_list[thumb_tip].y >  lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y:
        print("NÃO CURTI")
        cv2.putText(img, "NÃO CURTI", (20, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)