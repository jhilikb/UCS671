#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()
pub = None

def run_inference(img):
    # Replace with Dusty Inference logic
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Example: grayscale

def image_callback(msg):
    cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
    processed = run_inference(cv_image)
    ros_image = bridge.cv2_to_imgmsg(processed, encoding="mono8")
    pub.publish(ros_image)
    #cv2.imshow("Processed Image", processed)
    #cv2.waitKey(1)

def processor_node():
    global pub
    rospy.init_node("processor_node")
    pub = rospy.Publisher("/processed/image", Image, queue_size=10)
    rospy.Subscriber("/camera/image_raw", Image, image_callback)
    rospy.spin()

if __name__ == "__main__":
    processor_node()
