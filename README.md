# sign-language-identifier
  In this project we have created a Sign Language Identifier from scratch to detect various gestures used in sign language. The Model has achieved  89.50 precision. The code for the Transfer Learning Model is in the train.ipynb file. We have also presented the transfer Learning model in this file.

# In order to work several packages are meant to be installed
  yolov5
  django
  pytorch
  opencv

# install requirements
  pip install opencv-python
  pip install django
  pip install torch
  git clone https://github.com/ultralytics/yolov5

# Things to note:
  The weights file contains the trained model. The output will be produced (best.pt)
  A complimenatry website has been prepared. You can use it if you wish to.


# for Training the model
  run the ipyb file and run all the cells and you will receive the weight file
  for detection in terminal cd yolov5
      python detect.py --weights {weight file} --source video/images
  for training in terminal cd yolov5
      python train.py --img 416 --batch 16 --epochs 100 --data '../data.yaml' --cfg ./models/custom_yolov5s.yaml --weights '' --name yolov5s_results  --cache
  for django cd NGO 
      python manage.py runserver

# website demo
  https://www.canva.com/design/DAFLJAWBhkY/0ZqQ0xzI-UE0ENR5xrvjTg/edit?utm_content=DAFLJAWBhkY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

# model output demo
  visit demo folder
