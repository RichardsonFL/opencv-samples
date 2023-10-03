import cv2
import os


def get_frames_video(video: str):
    assert video is not None, "You must pass a path to the video."
    assert os.path.exists("frames"), "The 'frames' folder does not exists!"

    cap = cv2.VideoCapture(video)
    currentframe = 1

    print("The frames will be extracted to the 'frames/' folder...")
    while(True):
        hasFrame, frameImg = cap.read()
        if(hasFrame):
            outputFileName = f"frames/frame_{currentframe}.png"
            cv2.imwrite(outputFileName,frameImg)
            currentframe += 1
        else:
            break

    print("Frames extracting has been finished!")


if __name__ == '__main__':
    get_frames_video('../data/videos/samples.mp4')
    
