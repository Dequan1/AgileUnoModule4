# DeQuan Williams
# Module 4 Assignment

from sys import exit
from random import randint

#dictionary
myData = {}

#variable
guesses = 0

#variable
wins = 0


#context manager
with open ("questions.txt","r")as infiles:
    questions=infile.readlines()
    
# for loop
    for questions in questions:
# if statement        
        if "first" in question:
            myData["first_name"]=input(question)
        elif "last" in question:
            myData["last_name"]=input(question)
        else:
            print("bad question in input file")
            exit()

#for loop
    for play in range(10)
        number=randint(0,100)
        solved=false
#while loop    
    while not solved:
        guess=int(input(f"Guess a number from 0 to 100:"))
        guess+=1
# if statement        
        if guess == number
        print(f"Great Job{myData["first_name"],your guess of {guess} is correct!!!")
        wins+-1
        solved = True
#break        
        break
# if statement    

    if guess == number:
        print(f"Your guess of {guess}is incorrect!")
        if guess>number:
        print(f"Sorry, you guessed too high!!")
        elif guess<number:
        print(f"Sorry, you guessed to low!!")
        else:
#pass or null statement                   
                    
        pass

    if solved:
        print(f"Lets play again, you have completed {wins} out of 10 plays.")
# continue returns to the beginning of the loop        
        continue
    print(f"{myData["first_name]} {myData["last_name]}guessed the correct number {wins} out of (10 plays.")
    print(f"it took {myData["first_name]} {myData["last_name]} {guesses} guesses to do this!")
    exit()                                       
                                          
        
