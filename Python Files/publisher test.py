#!/usr/bin/env python
import queue
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    curr = "stop"
    q = queue.SimpleQueue(maxsize=0)
    while not rospy.is_shutdown():
        """
        take voice input
        decode voice command
        place important commands into queue with q.put_nowait(item) where item is the item to put onto queue-> if you get stop, 
        clear queue then break from decode
        e.g. q.put_nowait("stop")
        
        How to clear queue- copy this code, 
        while(not q.Empty()):
            q.get_nowait()
        """
        #Check if queue is empty, if it is- set curr to stop, if it isn't set it to next element in queue
        
        if (q.empty()):
            curr = "stop"
        else:
            curr = q.get()
        in_str = curr % rospy.get_time()  
        print(in_str)#test print remove later
        rospy.loginfo(in_str)
        pub.publish(in_str)
        rate.sleep()




if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass