import cv2,os,urllib.request
import numpy as np
from django.conf import settings
class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()#video read image-video var 

code goes here


		frame_flip = cv2.flip(image,1)#mirror of final image
		ret, jpeg = cv2.imencode('.jpg',frame_flip)#Video to html stream
		return jpeg.tobytes()#sending video
