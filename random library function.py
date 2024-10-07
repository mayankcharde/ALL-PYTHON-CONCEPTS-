import random  
def game():
    print("you are playing the game ...")
    score = random.randint(1,62)
    
    with open ("score.txt") as f :
        hisscore =f.read()
        if(hisscore!=""):

            hisscore = int(hisscore)
            
        else:
            hisscore =0
            
        print(f"your score:{score}")    
        if(score>hisscore):
         with open ("score.txt" , "w") as f :
             f.write(str(score))
             
             return score 
         
game()
