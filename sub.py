#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu


def imu_callback(msg):
    print ("------------------------------------------------")
    print ("veloc angular z = " + str(msg.angular_velocity.z))
    print ("veloc angular y = " + str(msg.angular_velocity.y))
    print ("aceleracion linear x = " + str(msg.linear_acceleration.x))
    print ("aceleracion linear y = " + str(msg.linear_acceleration.y))
    rate.sleep()


while not rospy.is_shutdown():
    rospy.init_node('imu_sub') 
    sub_imu = rospy.Subscriber('/imu', Imu, imu_callback)
    rate = rospy.Rate(1)
    rospy.spin()
