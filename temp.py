import cv2
import os
listing = os.listdir(r'D:/Images/AllVideos')
count=1
for vid in listing:
    vid = r"D:/Images/AllVideos/"+vid
    vidcap = cv2.VideoCapture(vid)
    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite("D:/Images/Frames/image"+str(count)+".jpg", image) # Save frame as JPG file
        return hasFrames
    sec = 0
    frameRate = 0.5 # Change this number to 1 for each 1 second
    
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)