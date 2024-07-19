#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random

def dice_roll():
     
    score = random.randint(1, 6)
    
    return score

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, please enter a number!")

max_score = 50

player_scores = [0] * players

while max(player_scores) < max_score:
    for i in range(players):
        print("\nplayer", i + 1, "turn has started!!\n")
        current_score = 0


        while True:
            ask_roll = input("Would you like to roll? enter 'y' if want to roll..")
            if player_scores[i] + current_score >= max_score:
                break
            if ask_roll.upper() != 'Y':
                break
            
            
            value = dice_roll()
            if value == 1:
                print("You got a 1, your turn is done!!")
                
                break
            else:
                current_score += value
                print("You rolled a: ", value)
    
            print("Your current_score is: ", current_score)
        player_scores[i] += current_score
        print("Yout total score is: ", player_scores[i])   

max_score = max(player_scores)   
winning_idx = player_scores.index(max_score)  
print("Player number ", winning_idx + 1, "is the winner with a score of: ", max_score)   




        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




