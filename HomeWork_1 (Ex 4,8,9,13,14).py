#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import time
import math
import csv
decision=50
flag=10
print("HI")
print("Ненужный текст")
print("\n")
print("This is rps game. Rules are simple: rock beats scissors, scissors beat paper and paper beats rock")
print("\n")
print("You will be able to play with you friend consequenty. If you want to play print 1, if you don't want to play, print 0")
decision=int(input())
while(decision!=0):
    if(decision==1):
        print("Player 1, ready!\n")
        print("Choose your element:\n")
        print("Print 1 to choose scissors\nPrint 2 to choose rock\nPrint 3 to choose paper")
        player1_decision=int(input())
        print("Player 2, ready!\n")
        print("Choose your element:\n")
        print("Print 1 to choose scissors\nPrint 2 to choose rock\nPrint 3 to choose paper")
        player2_decision=int(input())
        if(player1_decision-player2_decision==1) or (player1_decision==1 and player2_decision==3):
            print("Player 1 is the winner!!!\n")
            flag=0
        if(player1_decision==player2_decision):
            print("It is a tie\n")
            flag=1
        if((player2_decision-player1_decision==1) or (player2_decision==1 and player1_decision==3)):
            print("Player 2 is the winner!!!\n")
            flag=0
        if(flag==0):
            print("Do you wanna play again?\nIf you answer is yes, print 1, if no, print 0\n")
            decision=int(input())
print("THE END")
        
        
        
        


# In[ ]:


import numpy as np
import time
import math
import csv
import random
random_numb=0
guess=15
flag=1
game=50
decision=50
print("Hi, today we are playing a guessing game!\nI will generate a number between 0 and 9 \n")
print("Your task is to try to guess it. Let's go!\n Print 1 when you are ready.")
while(decision!=0):
    while (game!=1):
        game=int(input())
    if(game==1):
        random_numb=random.randint(0,9)
    print("All right, my number is ready. Don't try to cheat, it is impossible hahahahahaha\n")
    print("Input the number you are thinking of\n")
    while(flag==1):
        guess=int(input())
        if(guess==random_numb):
            flag=0
            print("You are correct\n")
        else:
            flag=1
            print("Incorrect, try again\n")
    print("Good job! You wanna try again?\nPrint 1 to continue or 0 to end")
    decision=int(input())
    flag=1
print("END")


# In[ ]:


import numpy as np
import time
import math
import csv

quantity=0
x=[]
res=0
print("Сколько чисел вам надо?")
quantity=int(input())
x.append(1)
x.append(1)
for i in range(quantity):
    if(i>1):
        res=x[i-1]+x[i-2]
        x.append(res)
print(x)


# In[ ]:


import numpy as np
import time
import math

def isInt(n):
    return int(n) == float(n)

number=0
res=0
x=[]
print("Введите ваше число")
number=int(input())
for i in range(number):
    if(i!=0):
        res=number/i
        if(isInt(res)==True):
            x.append(i)
print(x)


# In[ ]:


import numpy as np
import time
import math
import csv

def isInt(n):
    return int(n) == float(n)

flag=1
y=[]
while(flag==1):
    print("Хотите ли вы добавить элемент")
    decision=int(input())
    if(decision==1):
        elem=int(input())
        y.append(elem)
    if(decision==0):
        flag=0
print(y)
n=len(y)
p=[]
for i in range(n):
    if(isInt(y[i]/2)==True):
        p.append(y[i])
print(p)


# In[ ]:




