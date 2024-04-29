questions=[
   "1.What is value of print('2+2')? ",
    ["a.4","b.22","c.2+2"],
    "c",
    "2.What is value of print(2&2)?",
    ["a.22","b.2","c.4"],
    "b",
    
]
score=0
print(questions[0])
print('\n'.join(questions[1]))
answer=input("Enter your answer: ")
if answer==questions[2]:
    score+=1
    print("You earned a point.")
else:
    print("You didn't earned a point.")
    
print(questions[3])
print('\n'.join(questions[4]))
answer=input("Enter your answer: ")
if answer==questions[5]:
    score+=1
    print("You earned a point.")

else:
    print("You didn't earned a point.")

print("Quiz Ended.\nYour Point:",score)

