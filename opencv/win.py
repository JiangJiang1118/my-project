import cv2

cv2.namedWindow('new',cv2.WINDOW_NORMAL)#cv2.WINDOW_NORMAL是指窗口大小根据用户设置的大小调整,可以resize
cv2.resizeWindow('new',480,480)#设置窗口大小为640x480
cv2.imshow('new',0)#这里的0是指窗口中显示的图像，可以是任意的图像，这里设置为0表示显示黑色图像
key=cv2.waitKey(0)
if key=='q':#按q键退出
    exit()
    cv2.destroyAllWindows