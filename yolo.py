from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.predict(source="E:\pandaimage.png",save=True,show=True)
