import random
from data import  question_data

questnumber=1
score=0
live=5
Questlist = random.sample(question_data,10)

def gameover(score):
    print(f"Game over your score is {score}")
    quit()

for i in Questlist:
    print(f"{questnumber}-"+i["text"]+" T/F")
    ans = input()
    if ans == "T" or ans == "t":
        ans = "True"
    else:
        ans = "False"

    if i["answer"] == ans:
        print("True")
        score += 1
        print(f"Your score is {score}/{questnumber}")
    else:
        print("False")
        print(f"Your score is {score}/{questnumber}")
        live -=1
        print(f"You have {live} live ")
    if questnumber - score == 5:
        gameover(score)

    questnumber += 1
