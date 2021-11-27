#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #take voice input
        #decode voice command
        in_str = input("enter input:") % rospy.get_time()  #replace with decoded voice command
        #for now assume only 1 word is inputted and that it can be an invalid command
        rospy.loginfo(in_str)
        pub.publish(in_str)
        rate.sleep()
#For multiple commands
#TODO
#1. implement a queue
#2. for every valid word, push to back of the queue
#3. Every iteration take top of queue set current variable and send to ROS
#4. if queue is empty, send current again



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass