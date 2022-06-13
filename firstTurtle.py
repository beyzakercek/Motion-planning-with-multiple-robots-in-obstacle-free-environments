#!/usr/bin/env python

#chmod u+x ~/catkin_ws/src/beginner_tutorials/src/firstTurtle.py

import rospy
import sys
import math
from geometry_msgs.msg import Twist

nodeid = str(sys.argv[1])
nodename = "turtle" + nodeid
rospy.init_node(nodename, anonymous=True)
pub = rospy.Publisher(nodename +'/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()
def moveRobot(unit):
	#This function is used for the turtle to move linearly depends on unit parameter.
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0

	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0	
	rate = rospy.Rate(10)
	t0 = rospy.Time.now().to_sec()	
	current_distance = 0 
	

	while current_distance < unit:
		pub.publish(vel_msg) #publish velocity message
		t1 = rospy.Time.now().to_sec() 
		current_distance = vel_msg.linear.x * (t1-t0)
		rate.sleep()
	stop()

def down():
	#This function is used for the turtle move down.
	unit = 0.2
	rate = rospy.Rate(10)
	rospy.loginfo("Moving...")
	vel_msg.linear.x = 0.1
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0

	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0 
	t0 = rospy.Time.now().to_sec()
	current_distance = 0 

	while current_distance < unit:
		
		pub.publish(vel_msg) 
		t1 = rospy.Time.now().to_sec()
		current_distance = vel_msg.linear.x * (t1-t0)
		rate.sleep()

	stop()

def rotate(angle):
	#This function is used to rotate the turtle.
	speed = 10
	clockwise = -1
	linear_speed = 0

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

def stop():
	#This function is used to stop the turtle.
	vel_msg.linear.x = 0.0
	vel_msg.angular.z = 0.0
	pub.publish(vel_msg)

def angleFunc(direction):
	#This function is used to determine the angle of rotation of the turtle.
	rotationAngle =0
	if direction == 1: #R
		rotationAngle = 90

	elif direction == 2: #L
		rotationAngle = 270
	else:
		rospy.loginfo("No direction selected")	
	return rotationAngle

def round1(first_round_distance,first_round_direction):
	#For round1
	moveRobot(first_round_distance)
	rotate(angleFunc(first_round_direction))
	down()
	rotate(angleFunc(first_round_direction))
	moveRobot(first_round_distance)
	rotate(angleFunc(2)) 
	down()
	rotate(angleFunc(2))

def round2(first_round_distance,first_round_direction,second_round_distance,second_round_direction):
	#For round2
	if(first_round_direction == second_round_direction):
		second_round_distance = first_round_distance + 0.1
	else:
		second_round_distance = first_round_distance * 2

	rospy.loginfo(second_round_distance)

	moveRobot(second_round_distance)
	rotate(angleFunc(second_round_direction))
	down()
	rotate(angleFunc(second_round_direction))
	moveRobot(second_round_distance)
	return second_round_distance

def round3(third_round_distance,third_round_direction, second_round_distance,second_round_direction):
	#For round3
	if(second_round_direction == third_round_direction):
		third_round_distance = second_round_distance + 0.1
	else:
		third_round_distance = second_round_distance * 2

	rospy.loginfo(second_round_distance)
	moveRobot(third_round_distance)
	rotate(angleFunc(third_round_direction))
	down()
	rotate(angleFunc(third_round_direction))
	moveRobot(third_round_distance)
	

if __name__ == "__main__": 
	try:	
		first_round_distance = 0.4
		second_round_distance = 0
		third_round_distance = 0
		
		first_round_direction = 1 #R
		second_round_direction = 1 #R
		third_round_direction = 2 #L

		round1(first_round_distance,first_round_direction)
		second_round_distance = round2(first_round_distance,first_round_direction,second_round_distance,second_round_direction)
		round3(third_round_distance,third_round_direction, second_round_distance,second_round_direction)

	except rospy.ROSInterruptException:
		pass


