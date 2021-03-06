print("Title of program: Math Revision Game")
print("To complete this game you have to answer 3 questions correctly")
print("You have 5 tries to complete this game")
print("Answers with decimal places round to 1 s.f.")
print()

import random
from math import log10, floor
def round_to_1(x):
  return round(x, -int(floor(log10(abs(x)))))
counter = 0
score = 0
total_num_of_qn = 3

counter += 1
tracker = 0

while tracker != total_num_of_qn:

  #generate random number
  num1 = random.randint(1,10)
  num2 = random.randint(1,10)
  
  #generate random operation
  operator_choice = ['+', '-', '*', '/']
  operator = random.choice(operator_choice)
  
  #print question
  print("Q"+str(counter)+") " + "What is " + str(num1) + " " + str(operator) + " " + str(num2) + "?")
  
  #get answer
  answer = input("Your answer: ")
  answer = float(answer)
  
  #generate answer
  if operator == "+":
    a = num1 + num2
  elif operator == "-":
    a = num1 - num2
  elif operator == "*":
    a = num1 * num2
  elif operator == "/":
    a = num1 / num2
    
    #round number to 1 sig fig
    a = round_to_1(a)
    
  #check if answer is correct
  if answer == a:
    
    #if correct congrats +1 score, +1 tracker and +1 counter
    print("Congratulations! Your answer is correct!")
    score +=1
    tracker +=1
    counter +=1
  else:
    
    #if wrong sorry -1 score, +1 counter
    print("Wrong answer! Try again!")
    print("The answer is " + str(a))
    score -=1
    counter +=1
    
  #Limit tries
  if counter == 6:
    print("Your 5 tries is up.")
    break
    
  #print score in percentage
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )

#Different Congratulation text for different scores
if score == 3:
  Congrats = "Good job!"
elif score == 2:
  Congrats = "Nice try!"
elif score == 1:
  Congrats = "You can do better!"
elif score <= 0:
  Congrats = "Try again!"

#print overall score
print("You scored " + str(score) + " out of " + str(tracker) + ". " +  Congrats)
