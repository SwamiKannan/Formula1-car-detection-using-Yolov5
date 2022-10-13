## Process the data
### Creating snapshots from the videos
Move the videos to /train/videos
run create_images.py in the root folder
'''
python create_images.py
'''
Note: By default, the script is defined to collect 10 snapshots uniformly distributed across the video. Change the sample_count parameter in create_images.py if you want more or less samples per video

Move all images downloaded from Google to the /train/images folder

### Tagging the images
Label Studio https://github.com/heartexlabs/label-studio
(a) Install label studio
'''
pip install label-studio
pip install pyqt5 lxml --upgrade
cd labelImg
pyrcc5 -o libs/resources.py resources.qrc
'''

### Run LabelImg
Go to "labelImg\data"
Create a copy of the pre-defined_classes.txt, maybe, pre-defined_classes_backup.txt
Replace pre-defined_classes.txt with this version <predefined_classes.txt>
run labelImg.py
'''
cd LabelImg
python labelImg.py
'''

Set "Open Dir" to where image snapshots are stored
Set "Change Save Dir" to where you want to store the features
Set format to "YOLO" (8th icon from the top may say "YOLO", "CreateML" or "PascalVOC". Clicking on the icon changes the format as required)
Use left click to draw the bounded box on the image. Refer <https://github.com/heartexlabs/labelImg#readme> for usage guidelines

### Image Augmentation
Check the distribIution of the classes from the labels defined
'''
cd <output folder as chosen by Change Save Dir option in labelImg software
copy *.txt all_boxes.txt
'''

If you open all_boxes.txt, it will have the list of the bounding boxes created from the LabelImg software.
Extract the first column (I did it in Excel / Pandas) and plot a pivot for all the classes
Identify which classes require additional images are required and download them again. 