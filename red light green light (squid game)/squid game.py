import random #imports the random function
players = 75 #total players
count = 5 #counter
total_eliminated = 0
print("Welcome to red light green light")
while count > 0:
    light = str(input("Green light or red light?")).upper()
    if light == "RED LIGHT":
        eliminated = random.randint(1, 15)
        count = count - 1
        print ("The people who are eliminated are : ", eliminated)
        alive = players-eliminated
        print("The people alive are : ", alive)
        print("You can change the light ", count," More times")
        total_eliminated = total_eliminated + eliminated
        continue
    
    elif light == "GREEN LIGHT":
        count = count - 1
        print("You can change the light ", count," More times")
        continue
    elif light != "GREEN LIGHT" and light != "RED LIGHT":
        raise TypeError("Enter green light or red light")
print(print("The people alive are : ", alive))
print ("The people who are eliminated are (total) : ", total_eliminated)
        
