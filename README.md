# Roboflow Classification

## 1. 샘플 데이터셋 생성

### Image Files Upload

이미지 데이터셋이 있다면 아래의 메뉴를 통해 업로드

Projects > 기존 프로젝트 선택 (없다면 Create New Project) > Upload 메뉴에서 
가지고 있는 폴더 / 사진 업로드 또는 Drag and Drop

### 신규 프로젝트 생성

Object Detection으로 타입 설정후 나머지 내용은 임의로 작성

### Universe 에서 가져오기
- Object Detection 타입 클릭후 데이터셋 선택
- Image 메뉴 선택
![](./img/Load-From-Universe-1.png?raw=true)
- 원하는 이미지 선택
- Clone xx Selected Image 선택
![](./img/Load-From-Universe-2.png?raw=true)
![](./img/Load-From-Universe-3.png?raw=true)
- 담기 원하는 프로젝트 선택
![](./img/Load-From-Universe-4.png?raw=true)
- Import Images And Annotations 옵션 선택
- Finish Cloning XX Images 선택

## 2. 라벨링 방법

이미지 업로드 후 Apply를 하면 Annotation 할 수 있는 메뉴가 생성됨
이후 Annotation Tool 에서 다음과 같은 기능 수행 가능

### 1) 수동 - Roboflow의 Annotation Tool 이용
Annotation을 수동으로 진행할 수 있는 기능으로 다음이 있음

#### Bounding Box Tool
![](./img/Label-Hand-1.png?raw=true)
수동으로 바운딩 박스를 세팅하는 기능
드래그해서 선택 후 라벨링 지정


#### Polygon Tool
![](./img/Label-Hand-2.png?raw=true)
수동으로 세그멘테이션을 세팅하는 기능
포인트들 클릭 후 다시 원점 까지 눌러서 폐곡선 생성 후 라벨링 지정

#### Smart Polygon Tool
![](./img/Label-Hand-4.png?raw=true)
![](./img/Label-Hand-3.png?raw=true)
클릭한 이미지 기준으로 자동으로 부분 잡아오는 기능
부분 지정 후 라벨링 지정

### 2) 자동 - Universe에 있는 모델 이용하여 Annotation

#### Label Assistant Tool


* 먼저 Universe 에서 Model Tag 붙어있는 데이터 페이지 진입
![](./img/Label-Auto-With-Model-1.png?raw=true)
* 모델이름 왼쪽에 별모양 Star 클릭하여 check
![](./img/Label-Auto-With-Model-2.png?raw=true)
* Annotator 에서 Label Assist 클릭 후
![](./img/Label-Auto-With-Model-3.png?raw=true)
![](./img/Label-Auto-With-Model-4.png?raw=true)
* public 모델 선택 후 본인이 Star 누른 모델 중 선택
![](./img/Label-Auto-With-Model-5.png?raw=true)
* 해당 모델 선택 후 검출할 클래스 취사선택 가능
![](./img/Label-Auto-With-Model-6.png?raw=true)
* Let's Annotate 클릭

### 3) 여러 데이터셋 합치기
#### 1 - 프로그래밍적 방법
* 들어가기에 앞서 yolo8의 데이터셋 yaml 파일의 구조는 다음과 같다
```
train: ../train/images # train 데이터셋의 이미지 폴더
test: ../test/images # test 데이터셋의 이미지 폴더
nc: 3 # 이 데이터 셋이 가지고 있는 클래스의 갯수
names: ['0', '1', '2'] # 데이터 셋이 가지고 있는 클래스의 라벨링 이름
```

* Yolo8 기준으로 위와 같은 yaml 파일과 라벨텍스트를 수정하여 여러 데이터 셋을 합칠 수 있다.
    + 예시를 들면
    ```
    Dataset 1
    ㄴ data.yaml
    ㄴ train
       ㄴ image
       ㄴ labels
    ㄴ test
       ㄴ image
       ㄴ labels
    ```

    ```
    Dataset 2
    ㄴ data.yaml
    ㄴ train
       ㄴ image
       ㄴ labels
    ㄴ test
       ㄴ image
       ㄴ labels
    ```

위와 같은 폴더 구조의 두 묶음의 데이터셋이 있다고 가정하고
각각의 데이터셋의 yaml 파일의 구조는 다음과 같다 가정하면

```
Dataset 1 - data.yaml
train: ../train/images
test: ../test/images

nc: 2
names: ['human', 'human-fall']
```

```
Dataset 2 - data.yaml
train: ../train/images
test: ../test/images

nc: 1
names: ['human']
```

위의 경우 두 데이터 셋 모두 human 클래스가 0번째 인덱스로 존재하기 때문에 
Dataset 1에 Dataset 2를 엎어줘도 된다 

하지만 아래의 경우를 보면
```
Dataset 1 - data.yaml
train: ../train/images
test: ../test/images

nc: 2
names: ['Fire', 'Smoke']
```

```
Dataset 2 - data.yaml
train: ../train/images
test: ../test/images

nc: 1
names: ['Smoke']
```

Smoke 클래스가 1번 데이터셋의 경우엔 1번째 인덱스로 
2번 데이터셋의 경우엔 0번째 인덱스로 존재하기 때문에 이 내용을 맞춰주고 2번 데이터셋을 1번에 넣어주어야 한다.
라벨 텍스트의 경우 각 데이터셋 하위에 label이라는 폴더로 존재하며
txt 파일 각 행의 첫번째 숫자가 클래스 인덱스에 해당한다

label txt 파일 예시
```
0 0.4609375 0.58515625 0.75390625 0.6375  //  <object-class-id> <x> <y> <width> <height>
1 0.59296875 0.56484375 0.20625 0.8234375 // <object-class-id> <x> <y> <width> <height>
```
그러므로 위와 같은 경우엔 2번 데이터셋의 라벨맵의 첫 숫자를 1번 데이터셋에 맞게 0에서 1로 전부 변경시켜주어야 한다

마지막으로 아래와 같이 모두 다른 클래스를 가진 경우앤
```
Dataset 1 - data.yaml
train: ../train/images
test: ../test/images

nc: 2
names: ['Fire', 'Smoke']
```

```
Dataset 2 - data.yaml
train: ../train/images
test: ../test/images

nc: 1
names: ['Human']
```
1번 데이터셋에 2번 데이터 셋의 클래스가 없기 때문에 아래와 같이 data.yaml 파일을 우선 선언해준다
```
Dataset 3 - data.yaml
train: ../train/images
test: ../test/images

nc: 3
names: ['Fire', 'Smoke', 'Human']
```
그리고 라벨맵 또한 2번 데이터셋에선 0으로 쓰여졌지만 합치면서 휴먼 클래스들을 2로 전부 변경 후 1번 데이터 셋과 합쳐야 한다.

#### 2 - 로보플로우

![](./img/Merge-1.png?raw=true)
* 합치고자 하는 아무 프로젝트 한 개에 점 세 개 클릭 후 Merge Project
![](./img/Merge-2.png?raw=true)
* 합칠 프로젝트 추가 후 Merge 클릭

### 4) 임의의 라벨링 추가

2-1) 참조하여 사전 정의되지 않은 클래스도 추가 가능함.

## 3. 모델 학습

### 1) Roboflow 내에서 활용

![](./img/Roboflow-Train-1.png?raw=true)
* 어노테이션 완료된 프로젝트에서 Generate 클릭
![](./img/Roboflow-Train-2.png?raw=true)
* 소스 이미지 확인 (필요없거나 육안으로 품질 안좋은 이미지 제거해주시면 좋습니다)
![](./img/Roboflow-Train-3.png?raw=true)
* Train/Validation/Test Set 분리
![](./img/Roboflow-Train-4.png?raw=true)
* Rebalance 통해서 다르게 분배도 가능
![](./img/Roboflow-Train-5.png?raw=true)
* PreProcessing - 자동으로 회전된 이미지나 사이즈 크기 변경을 전처리
![](./img/Roboflow-Train-6.png?raw=true)
* 이외에도 다른 전처리도 가능 (유료기능인 것들은 화살표 표시)
![](./img/Roboflow-Train-7.png?raw=true)
* Augmentation의 경우 데이터셋이 모자라거나 여러 데이터를 이용할 수 있게 하기 위해 데이터셋의 이미지를 강제로 변형시키는 
* 여러 변형을 적용해 볼 수 있음 (유료기능인 것들은 화살표 표시)
![](./img/Roboflow-Train-8.png?raw=true)
![](./img/Roboflow-Train-9.png?raw=true)
* Generate를 누르고 Train With Roboflow 버튼을 눌러 모델 생성
![](./img/Roboflow-Train-10.png?raw=true)
* Fast 후 Continue / Accurate 는 유료
![](./img/Roboflow-Train-11.png?raw=true)
* 이전에 학습한 체크포인트 (중간 저장 모델) 혹은 퍼블릭으로 공개된 체크포인트로 학습 가능
![](./img/Roboflow-Train-12.png?raw=true)
* 학습완료되면 메일 노티와 함께 모델 사용 가능

### 2) User Define 학습 (YOLO8 기준)

#### 1 - Local Machine (우분투 22버전 기준)

##### 설치 및 체크

```bash
pip install ultralytics
```
를 통해 Yolo8 설치

```python
# check.py
import ultralytics
ultralytics.checks()
```
해당 코드를 통해 설치 잘 되었는지 확인

위에서 언급한 모양의 yaml 과 데이터셋을 만들어주고 학습시작
예시 폴더 구조 형태
```
 Dataset 1
    ㄴ data.yaml
    ㄴ train
       ㄴ image
       ㄴ labels
    ㄴ test
       ㄴ image
       ㄴ labels
```

##### 학습

```python
# train_ex.py
from ultralytics import YOLO
model = YOLO('yolov8n.pt')  # load a pretrained YOLOv8n detection model
model.train(data='/your_data.yaml', epochs=100, patience=30, batch=32, imgsz=416)
```
해당 코드를 통해 yaml 파일을 로드해와서 학습 시작


#### 2 - Cloud Machine

* AWS / GCP / Azure 등등에서 머신을 생성하는 데 있어서 Cuda Compatible Image가 포함된 os 설치 필요 
* 이후 작업은 1번 로컬 머신에서의 학습 방법과 동일     

## 4. 학습 모델 사용법 / 추론 (Inference)

아래 코드를 사용

```python
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
```

### Run (with Params)
```bash
python train.py
```

### Result 예시
```
{class num:counts} = {0.0: 1, 1.0: 1, 2.0: 2} 
```

### MultiModel User

* 각 모델별로 run_ex.py를 만들되 model.predict의 파라미터중 device에 gpu id 대입
* gpu id는 nvidia-smi 명령어를 통해 가능
