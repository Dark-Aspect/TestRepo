print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")

score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct")

    score += 1

else:
    print("Incorrect")

answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct")

    score += 1

else:
    print("Incorrect")

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct")

    score += 1
else:
    print("Incorrect")

answer = input("What does FORTRAN stand for? ")

if answer.lower() == "formula translation":
    print("Correct")

    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print("Correct")

    score += 1

else:
    print("Incorrect")

answer = input("What does UNIVAC stand for? ")

if answer.lower() == "universal automatic computer":
    print("Correct")

    score += 1
else:
    print("Incorrect")

answer = input("What does GPS stand for? ")

if answer.lower() == "global positioning system":
    print("Correct")

    score += 1

else:
    print("Incorrect")

answer = input("What does ATM stand for? ")

if answer.lower() == "automated teller machine":
    print("Correct")

    score += 1

else:
    print("Incorrect")

answer = input("What does ALU stand for? ")

if answer.lower() == "arithmetic logic unit":
    print("Correct")

    score += 1

else:
    print("Incorrect")

answer = input("What does Wi-Fi stand for? ")

if answer.lower() == "wireless fidelity":
    print("Correct")

    score += 1

else:
    print("Incorrect")

print("You got " + str(score) + " questions correct!")

print("You got " + str((score/10)*100) + "%.")

print("Thanks for Playing")