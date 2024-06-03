# 🔍 Spoofing Detector
 

## Banner
<p align="center">
  <img src="https://github.com/himaxx/Anti/blob/main/Back.jpg" width="500">
</p>

## UI
<p align="center">
  <img src="https://github.com/himaxx/Anti/blob/main/check.jpg" width="500">
</p>


This project focuses on detecting and classifying faces in real-time video streams as real or spoofed (fake) using computer vision techniques. The primary objective is to develop a robust system capable of distinguishing between authentic and spoofed faces, enabling potential applications in security, authentication, and related domains.

## 📚Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Explanations](#code-explanations)
- [Contributing](#contributing)
- [License](#license)

## 👀Project Overview
The Face Detection and Classification project aims to address the challenge of detecting and classifying faces in real-time video streams. It leverages the power of computer vision techniques and deep learning to differentiate between real and spoofed (fake) faces. This capability can be valuable in various scenarios, such as enhancing security measures, preventing identity fraud, and securing authentication systems.

## 📦Installation

1. Clone the repository:

 ```
  git clone https://github.com/himaxx/Anti.git
 ```

2. Installation of Dependencies:
 ```
  pip install opencv-python cvzone ultralytics
 ```
## 🚀Usage 
1. Data Collection: Run the data_collection.py script to collect and label face data from your webcam. The collected images and their corresponding labels will be saved in the Dataset/DataCollect directory.
   ```
   python data_collection.py
   ```
2. Dataset Splitting: Execute the split.py script to split the collected dataset into train, validation, and test subsets based on a specified ratio. The split data will be stored in the Dataset/SplitData directory, and a datao.yaml file containing the dataset paths and class names will be generated.
   ```
   python split.py
   ```
3. Model Training: Train the YOLOv8 object detection model using the train.py script. This script will load the split dataset from Dataset/SplitData/datao.yaml and train the model for a specified number of epochs.
   ```
   python train.py
   ```
4. Real-time Face Detection and Classification: After training is complete, run the main.py script to perform real-time face detection and classification using the trained model. The webcam feed will display the detected faces with bounding boxes and labels indicating whether they are real or spoofed.
   ```
   python main.py
   ```

## 📂Project Structure
 ```
 face-detection-classification/
├── Dataset/
│   ├── DataCollect/
│   └── SplitData/
|   └── Real/
|   └── Fake/
├── data_collection.py
├── split.py
├── train.py
├── main.py
└── README.md
 ```

## 💻Code Explanation

1. data_collection.py
This script is responsible for collecting and labeling face data from a webcam feed. It utilizes the OpenCV and cvzone libraries for face detection and image processing. The collected images and their corresponding labels are saved in the Dataset/DataCollect directory.

2. split.py
This script splits the collected dataset into train, validation, and test subsets based on a specified ratio. It creates the necessary directories under Dataset/SplitData and copies the images and labels accordingly. Additionally, it generates a datao.yaml file containing the paths to the split datasets and the class names.

3. train.py
This script trains a YOLOv8 object detection model using the Ultralytics library. It loads the split dataset from Dataset/SplitData/datao.yaml and trains the model for a specified number of epochs.

4. main.py
This script utilizes the trained YOLOv8 model to perform real-time face detection and classification on a webcam feed. It displays the detected faces with bounding boxes and labels (real or spoofed) on the video stream.

## 🤝Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
To contribute to this project, please follow these steps:
```
1.Fork the repository.
2.Create a new branch (git checkout -b feature/your-feature).
3.Make your changes and commit them (git commit -am 'Add some feature').
4.Push to the branch (git push origin feature/your-feature).
5.Create a new Pull Request.
```
