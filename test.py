from gpteams import gpteam

my_team = gpteam(number_of_workers=3, work_dir="output", question_file="questions/question1.py")

my_team.split_work()

my_team.merge_workers()


