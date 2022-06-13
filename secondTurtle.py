#!/usr/bin/env python

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/secondTurtle.py

import rospy 
import sys
import math
from geometry_msgs.msg import Twist

nodeid = str(sys.argv[1])
nodename = "turtle" + nodeid
rospy.init_node(nodename, anonymous=True)
pub = rospy.Publisher(nodename +'/cmd_vel', Twist, queue_size=10)
vel_msg = Twist() 
vel_msg.linear.x = 0
vel_msg.linear.y = 0
vel_msg.linear.z = 0	

vel_msg.angular.x = 0
vel_msg.angular.y = 0
vel_msg.angular.z = 0
 
def spiral(speed, angle, clockwise, linear_speed):
	#This function is used for the turtle to move in a sprial way
	roundNum = 0
	while(roundNum < 5):
		angular_speed = speed * (math.pi/180)
		relative_angle = angle * (math.pi/180)
		rate = rospy.Rate(10)
		vel_msg.linear.x = linear_speed
		vel_msg.angular.z = clockwise * abs(angular_speed)
	
		t0 = rospy.Time.now().secs
		current_angle = 0 

		while(current_angle < relative_angle):
			pub.publish(vel_msg)
			t1 = rospy.Time.now().secs
			current_angle = angular_speed * (t1-t0)
			rate.sleep() 

		stop() 
		linear_speed = linear_speed + 0.3
		roundNum = roundNum + 1


def stop():
	#This function is used to stop the turtle.
	vel_msg.linear.x = 0.0
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)
	

if __name__ == "__main__": 
	try:
		rospy.on_shutdown(stop)
		spiral(55.0, 180.0, -1, 0.2)

	except rospy.ROSInterruptException:
		pass

