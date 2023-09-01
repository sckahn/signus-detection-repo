# train_ex.py
from ultralytics import YOLO
model = YOLO('yolov8n.pt')  # load a pretrained YOLOv8n detection model
model.train(data='/your_data.yaml', epochs=100, patience=30, batch=32, imgsz=416)
# epoch - 학습횟수
# imgsz - 이미지 사이즈
# batch - 학습시 배치 사이즈
# patience - 학습이 길어졌을때 스코어의 차이가 별로 없을때 일찍 학습을 마무리

