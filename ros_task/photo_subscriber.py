#!/usr/bin/env python
#importing image message data type from sensors_msgs.msg
from sensor_msgs.msg import Image
#import cvbrdige to transform image to numpy for opencv
from cv_bridge import CvBridge
import numpy as np
import cv2 as cv
import rospy

class PhotoSharpening:

    def __init__(self):
        
        #node subscrition to the topipic /published_image 
        rospy.Subscriber('/published_image', Image, self.callback)
        #node publisher /sharpened_image topic 
	self.sharpened_publisher = rospy.Publisher("/sharpened_image", Image, queue_size=10)

    def callback(self, data):
        #cv bridge initiation
        bridge = CvBridge()
        #converting from Image to numpy array
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
        #kernel for sharpeneing
        kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        #sharpening using opencv
        sharpened=cv.filter2D(cv_image,-1,kernel)
        #displaying original vs sharpened
        cv.imshow("published_photo",cv_image)
        cv.imshow("sharpened_photo",sharpened)
        #converting from numpy array to image message
        sharpened = bridge.cv2_to_imgmsg(cv_image,encoding="bgr8")
        #publishing the sharpened image
        self.sharpened_publisher.publish(sharpened)
        #waits until node is terminated to terminate windows
        cv.waitKey(1)

if __name__ == '__main__':
    #node initiation
    rospy.init_node('photo_sharpening', anonymous=False)
    #class instance
    PhotoSharpening()
    #stop the node from being terminated
    rospy.spin()        
        
