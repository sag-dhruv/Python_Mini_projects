'''
Number guessing game
'''

import math, random


l = int(input()) #lower bound
u = int(input()) #upper bound

# random number
x = random.randint(l,u)
# no. of chances
chances = round(math.log(u - l+1,2))

print(f'You have only {chances} attempts to guess the number')
print("\U0001f44d")

count = 0

while count<chances:
      
    guess = int(input('\nEnter number: '))
    
   
    if x==guess:
        count+=1
        print('You guess correctly with no. of counts {} \U0001f60e'.format(count))
    
        
        break
    elif guess<x:
        count+=1
        print(f'You guessed too small \U0001f44e')
        
    elif guess>x:
        count+=1
        print(f'You guessed too high \U0001f44e')
            
    if count>=chances:
        print('Better luck next time')
        print('Sorry no of guesses over')   
        print("\U0001f44e")
        
        
    
    
    
    

