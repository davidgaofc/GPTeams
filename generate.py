from gpteams import gpteam
import os
import time


for question in os.listdir("questions"):
    my_question = question.split(".")[0]
    for i in range(1,4):
        my_team = gpteam(number_of_workers=i, work_dir="output/"+my_question+"/"+ "n" + str(i), question_file="questions/"+question)
        my_team.split_work()
        if(i > 1):
            my_team.merge_workers()



