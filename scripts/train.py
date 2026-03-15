from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolov8n.pt")

# 开始训练
model.train(
    data="coco8.yaml",
    epochs=5,
    imgsz=640
)
