welcome_message = "Welcome to the Quiz Game!"
score = 0

print(welcome_message)
while True:
    action = input("\nChoose one of the following topics and let's start the game!\n1. Animals\n(Other topics are coming soon!)\nEnter the number of the topic chosen: ")

    if action == "1":
        print("\nTopic: Animals\nWhich of these animals is actually a marsupial (carries its young in a pouch)?\nA) Giant Panda\nB) Koala\nC) Sloth\nD) Anteater")
        answer1 = input("\nEnter the letter to answer: ")
        if answer1 == "b" or answer1 == "B":
            print("Correct! Next question.")
            score += 1
        else:
            print("Incorrect! Next question.")
        
        print("\nWhat is the only mammal capable of true, powered flight?\nA) Flying Squirrel\nB) Ostrich\nC) Bat\nD) Sugar Glider")
        answer2 = input("\nEnter the letter to answer: ")
        if answer2 == "c" or answer2 == "C":
            print("Correct! Next question.")
            score += 1
        else:
            print("Incorrect! Next question.")

        print('\nWhich big cat is the only one that typically lives and hunts in social groups called "prides"?\nA) Tiger\nB) Leopard\nC) Cheetah\nD) Lion')
        answer3 = input("\nEnter the letter to answer: ")
        if answer3 == "d" or answer3 == "D":
            print("Correct!")
            score += 1
            print("You scored " + str(score) + "/3")
        else:
            print("Incorrect!")
            print("You scored " + str(score) + "/3")
        
        new_action = input("Do you want to continue the quiz with another topic?\nEnter Y to continue or N to exit the game: ")
        if new_action == "n" or new_action == "N":
            print("See you next time!")
            break
        else:
            score = 0
            continue

    
