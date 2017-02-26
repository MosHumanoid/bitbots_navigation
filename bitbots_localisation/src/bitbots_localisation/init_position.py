#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped


class InitPosition:
    def __init__(self):
        self.pose = rospy.Publisher("/initialpose", PoseWithCovarianceStamped, queue_size=1)
        rospy.init_node("init_pose")

    def init_pose(self):
        pose = PoseWithCovarianceStamped()
        pose.pose.pose.position.x = 0
        pose.pose.pose.position.y = 0
        pose.pose.pose.position.z = 0
        self.pose.publish(pose)


if __name__ == "__main__":
    ip = InitPosition()

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        ip.init_pose()
        rate.sleep()


