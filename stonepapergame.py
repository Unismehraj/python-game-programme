import random
l=['rock','paper','secissor']
cchoice=random.choice(l)
while True:
    ucount=0
    ccount=0
    ui=int(input('''
    press1 to playgame
    press2 to exit
    :-'''))
    if ui==1:
        print("welcome")
        for n in range(1,6): 
            userinput=(int(input('''
            press the correspoding key to select the option
            1.rock
            2.paper
            3.secissor
            :-''')))
            if  userinput==1:
                uchoice="rock"
            elif userinput==2:
                uchoice="paper"
            elif userinput==3:
                uchoice="secissor"
            
            if uchoice==cchoice:
                
                print("your value",uchoice)
                print("computer value",cchoice) 
                print("draw match") 
                ucount=ucount+1
                ccount=ccount+1
                       
            elif uchoice=="paper" and cchoice=="rock" or uchoice=="rock" and cchoice=='secissor'or uchoice=="secissor"and cchoice=="paper":
                 
                print("your value",uchoice)
                print("computer value",cchoice)
                print('you win')
                ucount=ucount+1
            else:
                
                print("your value",uchoice)
                print("computer value",cchoice)
                print("you lose")
                ucount=ccount+1
        if ucount==ccount:
            print("final match draw")
            print("your score",ucount)
            print("computer score",ccount)
        elif ucount>ccount:
            print("finally you won")
            print("your score",ucount)
            print("computer score",ccount)
        else:
            print("finally computer won")
            print("your score",ucount)
            print("computer score",ccount)
        
    else:
        break
