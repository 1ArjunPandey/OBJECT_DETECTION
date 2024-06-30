# Bag Detection and Counting on Conveyor Belt

This project implements an object detection and counting model to count the number of bags on a conveyor belt. The model is trained using custom-labeled data and leverages several popular machine learning and computer vision libraries.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to detect and count bags on a conveyor belt using a custom-trained object detection model. The model utilizes YOLO (You Only Look Once) for detection and various Python libraries for processing and tracking.

![final-gif](https://github.com/itsroshan137/Horizontal-Swiper/assets/134632401/29acf87c-8817-4569-a98b-42f520a8b28b)


## Technologies Used

- `cv2` (OpenCV): For image and video processing.
- `pandas` (`pd`): For data handling and manipulation.
- `YOLO` (from Ultralytics): For object detection.
- `tracker`: Custom tracker module for tracking detected objects.
- `cvzone`: For additional computer vision utilities.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/1ArjunPandey/OBJECT_DETECTION.git
   cd OBJECT_DETECTION
   
## Usage
Ensure your video data is placed in the data folder.

   

Run the object detection and counting script:
   ```
   python test.py

   ```

## Model Training

The model training for this project is performed using YOLO (You Only Look Once) in Google Colab. Follow these steps to train the model:


1. Upload your labeled dataset to Google Drive

2. Open the `yolov8_object_detection_on_custom_dataset.ipynb` notebook in Google Colab.

3. Mount your Google Drive and set up the notebook to access your dataset.

4. Run the notebook to train the YOLO model with your custom dataset.

5. After training, download the trained model weights and save them in the `models` directory of this repository.

For detailed instructions, refer to the `tyolov8_object_detection_on_custom_dataset.ipynb` notebook included in this repository.

    
This script will process the video and count the number of bags detected on the conveyor belt.

## Results
The model accurately detects and counts the number of bags on the conveyor belt. Below is an example of the output:

![final-gif](https://github.com/itsroshan137/Horizontal-Swiper/assets/134632401/29acf87c-8817-4569-a98b-42f520a8b28b)

