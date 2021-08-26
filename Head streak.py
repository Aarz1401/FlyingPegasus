import random
num_streak=0
list=[]

count=0
def flip(num):
    #code for flipping the coin n times
    for i in range(num):
      op=random.choice(["H","T"])
      list.append(op)
    return list
def count_streaks():
 streak_count=0
 count=1
 for i in range(len(list)-1):

         if list[i]==list[i+1]:
            count+=1
            if count==6:
               streak_count+=1
               count=0
         else:
            count+=0

 return streak_count
streak_yes=0

for i in range(100):
    flip(10)
    if count_streaks()>=1:
        streak_yes+=1
    list.clear()

print("Chance of streak of 6 is:",streak_yes/100)
# print(flip(100))
# print(count_streaks())









