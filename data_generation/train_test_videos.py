import cv2
import os
import random
import shutil
from video_utils import get_length



def train_test_split(all_list,shuffle_cnt=10):
    video_list=os.listdir(all_list)
    for _ in range(shuffle_cnt):
        random.shuffle(video_list)
    train_length=int(len(video_list)*0.8)
    train_list=video_list[:train_length]
    test_list=video_list[train_length:]
    print('Train test split done !')
    return train_list, test_list

def copy_files(train_list, test_list,train_path, test_path, all_list):
    for name in train_list:
        shutil.copyfile(os.path.join(all_list,name), os.path.join(train_path,name))
    for name in test_list:
        shutil.copyfile(os.path.join(all_list,name), os.path.join(test_path,name))

# train_list, test_list=train_test_split(ALL_VIDEOS_PATH,shuffle_cnt=100)
# copy_files(train_list, test_list,TRAIN_VIDEO_PATH, TEST_PATH, ALL_VIDEOS_PATH)



