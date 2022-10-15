import os
from train_test_videos import train_test_split, copy_files
from video_utils import get_clips

TRAIN_IMAGES_PATH=os.path.join('train',"images")
TRAIN_VIDEO_PATH=os.path.join('train',"videos")
TEST_PATH=os.path.join('test','videos')
ALL_VIDEOS_PATH=os.path.join('videos','all') 



#Create a train test split of videos and copy those videos into train or test folders
train_list, test_list=train_test_split(ALL_VIDEOS_PATH,shuffle_cnt=100)
print('Total number of videos to be sample images',len(train_list))
# copy_files(train_list, test_list,TRAIN_VIDEO_PATH, TEST_PATH, ALL_VIDEOS_PATH)
# print('Files copied !')

#Create clips from the files
cnt=0 
vids_cnt=len(train_list)
for vid in train_list:
    get_clips(vid,ALL_VIDEOS_PATH,TRAIN_IMAGES_PATH)
    cnt+=1
    if (cnt*100/vids_cnt)%10==0:
        print(f'{cnt} videos processed; {cnt*100/vids_cnt}% complete')
