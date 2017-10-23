#!/usr/bin/env python

from geometry_msgs.msg import Twist
import rospy
from sensor_msgs.msg import Joy


__maintainer__ = "Anthony Olive"
__email__ = "anthony@iris-systems.net"
__copyright__ = "Copyright 2016, MIL"
__license__ = "MIT"


rospy.init_node("joystick")

class Joystick(object):

    def __init__(self):

        rospy.Subscriber("joy", Joy, self.joy_recieved)
        self.wrench_pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=1)

    def publish_wrench(self, x, y, rotation, stamp=None, *args, **kwargs):
        '''
        Publishes a wrench to the specified node based on force inputs from the
        controller.
        '''
        if (stamp is None):
            stamp = rospy.Time.now()

        if (self.wrench_pub is not None):
            wrench = Twist()
            wrench.linear.x = x
            wrench.linear.y = y
            wrench.angular.z = rotation
            self.wrench_pub.publish(wrench)

    def joy_recieved(self, joy):

        # Scale joystick input to force and publish a wrench
        x = joy.axes[1] * .5
        y = joy.axes[0] * .5
        rotation = joy.axes[3] * 3
        self.publish_wrench(x, y, rotation, joy.header.stamp)


if __name__ == "__main__":
    joystick = Joystick()
    rospy.spin()
