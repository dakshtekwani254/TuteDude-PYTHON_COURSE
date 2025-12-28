#Module 9:Loops
#Video 10:Star pattern using for loops
#Practice 

for i in range(1,6):
  print(i*'* ')

#or using nester loops (as done in video)
print("________________________________________")

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
