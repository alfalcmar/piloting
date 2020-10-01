#!/usr/bin/env python
import rospy
# from uav_abstraction_layer.srv import TakeOff, Land
from geometry_msgs.msg import Twist, TwistStamped, PoseStamped
from nav_msgs.msg import Odometry

rospy.init_node('bag_visualizer', anonymous=True)


def cam1_pose_callback(data):
    data.header.frame_id = 'cam1_odom_frame'
    cam1_pub.publish(data)


def cam2_pose_callback(data):
    data.header.frame_id = 'cam1_odom_frame'
    cam2_pub.publish(data)

# def gps_pose_callback(data):
#     data.header.frame_id = 'map'
#     gps_pub.publish(data)

rospy.Subscriber('/cam1/odom/sample', Odometry, cam1_pose_callback, queue_size=1)
rospy.Subscriber('/cam2/odom/sample', Odometry, cam2_pose_callback, queue_size=1)
# rospy.Subscriber('/mavros/local_position/pose', PoseStamped, gps_pose_callback, queue_size=1)

cam1_pub = rospy.Publisher('/cam1/pose',Odometry, queue_size=1)
cam2_pub = rospy.Publisher('/cam2/pose',Odometry, queue_size=1)
# gps_pub = rospy.Publisher('/gps/pose',PoseStamped, queue_size=1)

rospy.spin()