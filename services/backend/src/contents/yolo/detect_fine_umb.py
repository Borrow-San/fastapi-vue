import os

import boto3
from src.env import ROOT_CTX
from yolov5 import detect

CURRENT_CTX = os.path.join(ROOT_CTX, "contents", "yolo")

BUCKET_NAME = 'bucket-aiacademy'
REGION_NAME = 'ap-northeast-2'
BUCKET_URL = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/borrowsan"
ACCESS_KEY = 'AKIA4FKKSBCF4BW3KPNG'
SECRET_KEY = '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'


def upload_image(filename, content):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    s3.put_object(Bucket=BUCKET_NAME, Key=filename, Body=content)


def detect_fine_umb(filename, content):
    upload_image(filename, content)
    detect.run(
        source=BUCKET_URL + filename,
        weights=os.path.join(CURRENT_CTX, "best_lee.pt"),
        conf_thres=0.25, imgsz=640, data=os.path.join(CURRENT_CTX, "data.yaml"),
        project=os.path.join(CURRENT_CTX, 'save'),
        name=filename, save_txt=True)
    if any(os.scandir(os.path.join(CURRENT_CTX, f"save/{filename}/labels"))) is True:
        return "멀쩡한 우산이 있습니다."
    else:
        return "멀쩡한 우산이 없습니다."
