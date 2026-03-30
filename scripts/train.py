from ultralytics import YOLO

# 加载预训练模型
model = YOLO("yolov8n.pt")

# 开始训练
model.train(
    data="vehicles.v2-release.yolov8/data.yaml",
    epochs=50,
    imgsz=640
)