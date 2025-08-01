print("-------Computer Quiz--------")
score=0
attempts=5

def printfunc(attempts ,score):
     print(f"You have {attempts} attempts and Score is {score}")
     if(attempts>=0 and score>=10):
         print("You have Won the game!\n")
         return True
     elif(attempts==0 and score<10):
        print("You have lost the game!\n")
        return False
     else:
         print("Game is On!\n")
         return True
     
playing=input("Do You want to Play? Yes|NO \n")
if(playing.lower()=="yes"):
    print("Okay! Let's Play\n")
elif(playing.lower()=="no"):
    print("Quitting Game\n")
    quit()
else:
    print("Please Enter a Valid Input\n")
    quit()




print("Entering the Game")
game=True
while game:
    answer=input("What is the capital of France?\n")
    if answer.lower()=="paris":
        print("Correct")
        score+=2
    else:
        print("Incorrect!")
        attempts-=1
        
        if not (printfunc(attempts,score)):
            break
    printfunc(attempts,score)
    answer2=input("what is 25-17?")
    if answer2=="8":
        print("Correct")
        score+=2
    else:
        print("Incorrect!")
        attempts-=1
        
        if not (printfunc(attempts,score)):
            break
    printfunc(attempts,score)
    answer3=input("What is the typeof 8+7i in Python")
    if answer3=="complex":
        print("Correct")
        score+=2
    else:
        print("Incorrect!")
        attempts-=1
        
        if not (printfunc(attempts,score)):
            break
    printfunc(attempts,score)        
    answer4=input("What will the the function returns bool([])?")
    if answer4=="False":
        print("Correct")
        score+=2
    else:
        print("Incorrect!")
        attempts-=1
        
        if not (printfunc(attempts,score)):
            break
    printfunc(attempts,score)
    answer5=input("What does CPU stands for?")
    if answer5.upper()=="Central Processing Unit":
        print("Correct")
        score+=2
    else:
        print("Incorrect!")
        attempts-=1

        if not (printfunc(attempts,score)):
            break
    printfunc(attempts,score)

print("Your Final Score is",score)
    


        

    