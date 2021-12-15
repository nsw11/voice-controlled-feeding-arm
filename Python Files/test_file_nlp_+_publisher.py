
#!/usr/bin/env python
import queue
import rospy
from std_msgs.msg import String

import speech_recognition as sr

r = sr.Recognizer()
command_set = {"undefined",'up','down',"right","left","forward","back","start","stop","power on", "power off"}
q = queue.SimpleQueue(maxsize=0)

def get_speech_to_text():
    words = []
    new_word = ''
    i = 0
    with sr.Microphone() as source:
        print('<<Miah is listening>>')
        r.adjust_for_ambient_noise(source, duration=1)
        audio_data = r.listen(source)
        print('Ok')
        try:
            text = r.recognize_google(audio_data)
            print("Google: "+text)
        except:
            text = ' '
            print('No commands detected')

        text = text + ' '  # for the last word to be recognized
    for letter in text:
        if letter != ' ':
            new_word = new_word + letter.lower()
        else:
            words.append(new_word)
            i = i+1
            new_word = ''
    return words


def command_interpretation():
    global q
    stopnot = 1
    input_text = get_speech_to_text()
    temp_command_matrix = []
    for word in input_text:
        i = 0
        for recognized_command in command_set:
            if word == recognized_command:
                temp_command_matrix.append(recognized_command)
                q.put_nowait(recognized_command)
                i = i+1

    print("Command Matrix: " + str(temp_command_matrix))

    write_command_to_file(' ', 'w')
    for commands in temp_command_matrix:
        write_command_to_file(str(commands+' '), 'a')

    return temp_command_matrix


def write_command_to_file(text, w_a):
    f = open("commands.txt", w_a)
    f.write(text)
    f.close()


def nlp_loop():
    global q
    command_matrix = command_interpretation()
    for commands in command_matrix:
        # exit criterion
        if commands == 'stop':
            while not q.Empty():
                q.get_nowait()


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    curr = "stop"

    while not rospy.is_shutdown():
        """
        making a change to test commits
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

        nlp_loop() # process the next audio input -> variable time function

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
