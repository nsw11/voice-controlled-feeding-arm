# Miah: a robot that feeds based on your needs
# Copyright: All rights proprietary: consult first Anahita / Nicholas / Shogair / Ravi
# You gotta pip install SpeechRecognition PyAudio Pydub
# For Pydub I had to first install pipwin, and use that instead of pip

import speech_recognition as sr
import queue


r = sr.Recognizer()
command_set = {"undefined",'up','down',"right","left","forward","back","start","stop","power on", "power off"}


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
            print('WTF you gotta be louder!')

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
    stopnot = 1
    input_text = get_speech_to_text()
    temp_command_matrix = []
    for word in input_text:
        i = 0
        for recognized_command in command_set:
            if word == recognized_command:
                temp_command_matrix.append(recognized_command)
                i = i+1

    print("Command Matrix: " + str(temp_command_matrix))

    write_command_to_file(' ', 'w')
    for commands in temp_command_matrix:
        write_command_to_file(str(commands+' '), 'a')
        # exit criterion
        if commands == 'stop':
            stopnot = 0

    return stopnot


def write_command_to_file(text, w_a):
    f = open("commands.txt", w_a)
    f.write(text)
    f.close()


def main_loop():
    stopnot = 1
    while stopnot == 1:
        stopnot = command_interpretation()


main_loop()

