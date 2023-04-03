import os
from src.env import ROOT_CTX
from yolov5 import detect

CURRENT_CTX = os.path.join(ROOT_CTX, "contents", "yolo")

def detect_fine_umb(filename):
    detect.run(
        source=os.path.join(ROOT_CTX, "data", "images", f"{filename}.jpg"),
        weights=os.path.join(CURRENT_CTX, "best_lee.pt"),
        conf_thres=0.25, imgsz=640, data=os.path.join(CURRENT_CTX, "data.yaml"),
        project=os.path.join(CURRENT_CTX, 'save'),
        name=filename, save_txt=True)
    if any(os.scandir(os.path.join(CURRENT_CTX, f"save/{filename}/labels"))) is True:
        return "멀쩡한 우산이 있습니다."
    else:
        return "멀쩡한 우산이 없습니다."

def test_detect_fine_umb(filename):
    detect.run(
        source=os.path.join(CURRENT_CTX, f"{filename}.jpg"),
        weights=os.path.join(CURRENT_CTX, "best_lee.pt"),
        conf_thres=0.25, imgsz=640, data=os.path.join(CURRENT_CTX, "data.yaml"),
        project=os.path.join(CURRENT_CTX, 'save'),
        name=filename, save_txt=True)
    if any(os.scandir(os.path.join(CURRENT_CTX, f"save/{filename}/labels"))) is True:
        return "멀쩡한 우산이 있습니다."
    else:
        return "멀쩡한 우산이 없습니다."

if __name__ == '__main__':
    print(test_detect_fine_umb("unnamed2"))
