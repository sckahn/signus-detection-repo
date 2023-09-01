# run_ex.py
from ultralytics import YOLO
from PIL import Image
import numpy as np


model = YOLO('yolov8n.pt')  # yolo8모델 다운로드 및 로드 // 커스텀모델 경로 대입
results = model.predict(source='./test_img_path/*.jpg', save=True) # test_img_path에는 inference 할 파일 경로 대입
for result in results:
        
    uniq, cnt = np.unique(result.boxes.cls.cpu().numpy(), return_counts=True)
    uniq_cnt_dict = dict(zip(uniq, cnt))

    print('\n{class num:counts} =', uniq_cnt_dict,'\n')

    for c in result.boxes.cls:
        print('class_name =', model.names[int(c)])
