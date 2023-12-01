from gpteams import gpteam
import os
import time

# done = [2,3,4,5,6,7,8,9,10]

for question in os.listdir("questions"):
    # print(str(question)[9])
    # if(int(str(question)[8]) != 1 and str(question)[9] != "."):
    #     continue
    if(question != "question1.py"):
        continue
    print("starting", question)
    my_question = question.split(".")[0]
    for i in range(1,4):
        my_team = gpteam(number_of_workers=i, work_dir="output/"+my_question+"/"+ "n" + str(i), question_file="questions/"+question)
        my_team.split_work()
        if(i > 1):
            my_team.merge_workers()
        print(i, "done")

    print("done with", my_question)



