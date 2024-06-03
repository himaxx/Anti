from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def main():
    model.train(data ="Testing Scripts/Dataset/SplitData/datao.yaml", epochs =3, batch =20)

if __name__ == '__main__':
    main()