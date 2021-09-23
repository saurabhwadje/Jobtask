from Question import Question

question_prompts=["Which one is correct team name in NBA?\nNew York Bulls\nLos Angeles Kings\nGolden State Warriros\nHuston Rocket\n\n",
"5 + 7 = ?\n10\n11\n12\n13\n\n",
"12 - 8 = ?\n1\n2\n3\n4\n\n"]
      
questions_1=[Question(question_prompts[0],"Huston Rocket")]
questions_2=[Question(question_prompts[1],"12"),
Question(question_prompts[2],"4")]

def run_test(questions):
    score=0

    for i in questions:
        answer=input(i.prompt)
        if answer==i.answer:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions))+" correct");

print("Choose a Group.(Enter option number)\n1.Sport\n2.Math")
number=input() 
if(number=='1'):
    run_test(questions_1)
if(number=='2'):
    run_test(questions_2)
