import random

def rolling():
    num=random.randint(1,6)
    if(num==1):
        print(" _____ ")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("|_____|")
    elif(num==2):
        print(" _____ ")
        print("|0    |")
        print("|     |")
        print("|    0|")
        print("|_____|")
    elif(num==3):
        print(" _____ ")
        print("|    0|")
        print("|  0  |")
        print("|0    |")
        print("|_____|")
    elif(num==4):
        print(" _____ ")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("|_____|")
    elif(num==5):
        print(" _____ ")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")        
        print("|_____|")
    elif(num==6):
        print(" _____ ")
        print("|0   0|")
        print("|0   0|")
        print("|0   0|")
        print("|_____|")



def ask():
    response=input("y to continue \nn to exit: ")

    if(response=='y' or response=='Y'):
        rolling()
        ask()
    elif(response=="n" or response=='N'):
        None
    else:    
        ask()

ask()


'''
Output

y to continue 
n to exit: y 
 _____ 
|0   0|
|  0  |
|0   0|
|_____|
y to continue
n to exit: y
 _____ 
|0   0|
|0   0|
|0   0|
|_____|
y to continue
n to exit: y
 _____ 
|    0|
|  0  |
|0    |
|_____|
y to continue
n to exit: n
'''