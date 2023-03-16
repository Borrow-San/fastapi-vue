import os

import shortuuid
from yolov5 import detect

from src.personal_constants import ROOT_CTX

CURRENT_CTX = os.path.join(ROOT_CTX, "contents", "yolo")


def yolov5_test(filename, content):
    with open(os.path.join(CURRENT_CTX, "data", filename), "wb") as fp:
        fp.write(content)
    dir_name = shortuuid.uuid()
    detect.run(source=os.path.join(CURRENT_CTX, "data", filename),
               weights=os.path.join(CURRENT_CTX, "best_lee.pt"),
               conf_thres=0.25, imgsz=640, data=os.path.join(CURRENT_CTX, "data.yaml"),
               project=os.path.join(CURRENT_CTX, 'save'),
               name=dir_name, save_txt=True)
    if any(os.scandir(os.path.join(CURRENT_CTX, f"save/{dir_name}/labels"))) is True:
        return "멀쩡한 우산이 있습니다."
    else:
        return "멀쩡한 우산이 없습니다."
