#!/usr/bin/env python
#importing image message data type from sensors_msgs.msg
from sensor_msgs.msg import Image
import rospy

class PublishPhoto:

    def __init__(self):
        #image topic to subscribe for
        img_topic = '/camera/rgb/image_raw'
        #node subscription to the image topic with callback function
        rospy.Subscriber(img_topic, Image, self.callback)
        #publisher to /published image
	self.image_publisher = rospy.Publisher("/published_image", Image, queue_size=10)

    def callback(self, data):
        #publishing the frames of the camera
        self.image_publisher.publish(data)

if __name__ == '__main__':
    #node initiation
    rospy.init_node('photo_publisher', anonymous=False)
    #class instance
    PublishPhoto()
    #stop the node from being terminated
    rospy.spin()        
        
