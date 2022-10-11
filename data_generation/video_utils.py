import os
import subprocess
import cv2
import uuid

#file_n="Charles Leclerc's Onboard Pole Lap ｜ 2022 Bahrain Grand Prix ｜ Pirelli [jSIAT0UYotQ].f303.webm"

def get_length(filename):
    '''
    You need to install ffmpeg for this function and set the PATH variable to point at ffmpeg's bin file
    args:
    filename - name of video file
    returns:
    length of the video file (in seconds)
    '''
    filename=os.path.join(filename)
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                "format=duration", "-of",
                                "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return int(float(result.stdout))


def get_clips(file_n,load_path,save_path,sample_count=10):
    cap=cv2.VideoCapture(os.path.join(load_path,file_n))
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    get_every=int(total_frames/sample_count)
    frame_nos=[(index+1)*get_every for index in list(range(sample_count))]

    while cap.isOpened():
        for frame_no in frame_nos:
            cap.set(cv2.CAP_PROP_POS_FRAMES ,frame_no)
            fr_exists,frame=cap.read()
            if fr_exists:
                cv2.imwrite(os.path.join(save_path,str(uuid.uuid1())+'.jpg'),frame)
            else:
                print('Frame doesnt exist')
        break
    cap.release()
    cv2.destroyAllWindows()
