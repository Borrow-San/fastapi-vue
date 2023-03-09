import os

import shortuuid
from yolov5 import detect

ROOT_CTX = "/app/src/services/yolo"


def yolov5_test(filename, content):
    with open(os.path.join(ROOT_CTX, f"data/{filename}"), "wb") as fp:
        fp.write(content)
    dir_name = shortuuid.uuid()
    detect.run(source=os.path.join(ROOT_CTX, f"data/{filename}"), weights=os.path.join(ROOT_CTX, "best_lee.pt"),
               conf_thres=0.25, imgsz=640, data=os.path.join(ROOT_CTX, "data.yaml"),
               project=os.path.join(ROOT_CTX, 'save'),
               name=dir_name, save_txt=True)
    if any(os.scandir(os.path.join(ROOT_CTX, f"save/{dir_name}/labels"))) is True:
        return "멀쩡한 우산이 있습니다."
    else:
        return "멀쩡한 우산이 없습니다."
