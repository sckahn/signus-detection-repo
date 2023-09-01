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
- Clone Image 선택
- 담기 원하는 프로젝트 선택
- Annotated 옵션 선택
- Clone!

## 2. 라벨링 방법

이미지 업로드 후 Apply를 하면 Annotation 할 수 있는 메뉴가 생성됨
이후 Annotation Tool 에서 다음과 같은 기능 수행 가능

### 1) 수동 - Roboflow의 Annotation Tool 이용
Annotation을 수동으로 진행할 수 있는 기능으로 다음이 있음

#### Bounding Box Tool
#### Polygon Tool
#### Smart Polygon Tool

### 2) 자동 - Universe에 있는 모델 이용하여 Annotation

#### Label Assistant Tool

* Universe 에서 Model Tag 붙어있는 데이터 페이지 진입 후
* Star Check
* Annotator 로 들어가면 해당 모델 체크가능
* 해당 모델 선택 후 검출할 클래스 취사선택 가능
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

합치고자 하는 아무 프로젝트 한 개에 점 세 개 클릭 후 Merge Project
합칠 프로젝트 추가 후 Merge 클릭

### 4) 임의의 라벨링 추가

2-1) 참조하여 사전 정의되지 않은 클래스도 추가 가능함.

## 3. 모델 학습

### 1) Roboflow 내에서 활용

### 2) User Define 학습

#### 1 - Local Machine
     
#### 2 - Cloud Machine
     

## 4. 학습 모델 사용법 / 배포

## 5. 추론 (Inference)

### Requirements

### Run (with Params)

### Result

### MultiModel User