import cv2
import ml as ml
import json
import re
import os
import camera


camera.configCamera()

fileDir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
outputDir = os.path.join(fileDir, "Output")
metaPath = os.path.join(outputDir,"metadata.json")
videoPath = os.path.join(fileDir, "vid.mp4")


def getFramePath(identifier: str) -> str:
    return os.path.join(outputDir,f'frame_{identifier}.jpg')

def runCam():
    camera.takePic()
    ml.runML()

def processVideo():
    #
    try:

        with open(metaPath,"r") as metadata: 
            files = json.load(metadata)
        if files:
            return files
    except FileNotFoundError as e:
        pass
    except json.decoder.JSONDecodeError as j:
        pass

    frameNr = 0
    #
    files = []
    capture = cv2.VideoCapture(videoPath)
    while(True):
        success, frame = capture.read()
        print(frameNr)
        if not success:
            break
        if success:
            framePath = getFramePath(frameNr)
            if (frameNr%30 == 0):
                cv2.imwrite(framePath, frame)
                #
                files.append(framePath)
        else:
            break
    
        frameNr = frameNr+1

    capture.release()
    #
    with open(metaPath,"w") as metadata: 
        json.dump(files,metadata)
    #
    return files
#
def processFrames(files: list[str])->None: 
    for file in files:
        #
        frameNum = [s for s in file.replace("_",".").split(".") if s.isdigit()][0]
        print(f'{ml.runML(file)},{frameNum}')
        #

if (__name__ == "__main__"):
    while (True):
        runCam()
    #files = processVideo()
    #processFrames(files)






