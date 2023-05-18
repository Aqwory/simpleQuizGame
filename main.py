print("Welcome to my quiz game where you can test your knowledge!")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Ooookaaayyyy lessgoo!")
print("NOTE: EVERY WORD IN ANSWERS SHOULD START WITH AN UPPERCASE LETTER")
score = 0

answer = input("What country has the highest life expectancy? ")
if answer == "Hong Kong":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Hong Kong")


answer = input("Where would you be if you were standing on the Spanish Steps? ")
if answer == "Rome":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is:")


answer = input("Which language has the more native speakers: English or Spanish? ")
if answer == "Spanish":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Spanish")


answer = input("What is the most common surname in the United States? ")
if answer == "Smith":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Smith")


answer = input("What disease commonly spread on pirate ships? ")
if answer == "Scurvy":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Scurvy")


answer = input("Who was the Ancient Greek God of the Sun? ")
if answer == "Apollo":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Apollo")


answer = input("What was the name of the crime boss who was head of the feared Chicago Outfit? ")
if answer == "Al Capone":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Al Capone")


answer = input("What year was the United Nations established? ")
if answer == "1945":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: 1945")


answer = input("Who has won the most total Academy Awards? ")
if answer == "Walt Disney":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Walt Disney")


answer = input("What artist has the most streams on Spotify? ")
if answer == "Drake":
    print("You got it right, let's move on!")
    score += 1
else: 
    print("The correct answer is: Drake")


print("You got " + str(score) + " question(s) correct!")
print("You got " + str((score/10) * 100) + "%")