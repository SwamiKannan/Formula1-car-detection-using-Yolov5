Model was built in <b> [Yolov5](https://docs.ultralytics.com/) </b>

## Yolo v5
YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents Ultralytics open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.


[yolov4 paper](https://arxiv.org/abs/2004.10934v1)
[yolov5 readme](https://docs.ultralytics.com/)
[yolov5 github](https://github.com/ultralytics/yolov5)

Custom training of yolov5 was done using [Yolov5's training page](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)

### Model
[yolov5m](https://github.com/ultralytics/yolov5#pretrained-checkpoints)

### Yaml file:
[dataset.yaml](

### Installation
Clone the Ultralytics Yolov5 repository
```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

### Training


Script (in yolov5 folder)

<ul><li> In conda / VS Code command prompt </li></ul>
```
cd yolov5
python train.py --img 320 --batch 16 --epochs 500 --data dataset.yml --weights yolov5s.pt --workers 2
```
<ul><li> In Jupyter notebook </li></ul>
```
!python cd yolov5 & train.py --img 320 --batch 16 --epochs 500 --data dataset.yml --weights yolov5s.pt --workers 2
```




Storing intermediate result in here only. For long term, it should be stored in model repository separately. Besides binary model, you should also store model metadata such as date, size of training data.