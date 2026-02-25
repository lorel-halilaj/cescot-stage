score = 0

def final_score():
    print("You scored " + str(score) + "/3")

print("Welcome to the Quiz Game!")
while True:
    action = input("\nChoose one of the following topics and let's start the game!\n1. Animals\n2. Cartoons\n3. Geography\nAlternatively enter ESC to exit the game.\nEnter the number of the topic chosen: ")

    #TOPIC 1
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
            final_score()
        else:
            print("Incorrect!")
            final_score()

    #TOPIC 2  
    elif action == "2":
        print("\nTopic: Cartoons\nIn the series The Simpsons, what color is the family's iconic car?\nA) Red\nB) Blue\nC) Pink\nD) Orange")
        answer1 = input("\nEnter the letter to answer: ")
        if answer1 == "c" or answer1 == "C":
            print("Correct! Next question.")
            score += 1
        else:
            print("Incorrect! Next question.")
        
        print("\nWhich of these Disney characters was the very first to be created?\nA) Donald Duck\nB) Mickey Mouse\nC) Goofy\nD) Pluto")
        answer2 = input("\nEnter the letter to answer: ")
        if answer2 == "b" or answer2 == "B":
            print("Correct! Next question.")
            score += 1
        else:
            print("Incorrect! Next question.")

        print("\nIn Adventure Time, what is the name of Finn the Human's magical adoptive brother?\nA) BMO\nB) Ice King\nC) Marceline\nD) Jake the Dog")
        answer3 = input("\nEnter the letter to answer: ")
        if answer3 == "d" or answer3 == "D":
            print("Correct!")
            score += 1
            final_score()
        else:
            print("Incorrect!")
            final_score()
    
    #TOPIC 3
    elif action == "3":
        print("\nTopic: Geography\nWhich of these is the largest continent on Earth by both land area and population?\nA) Africa\nB) North America\nC) Asia\nD) Europe")
        answer1 = input("\nEnter the letter to answer: ")
        if answer1 == "c" or answer1 == "C":
            print("Correct! Next question.")
            score += 1
        else:
            print("Incorrect! Next question.")
        
        print("\nThe Nile River, often cited as the longest river in the world, is primarily located on which continent?\nA) South America\nB) Africa\nC) Australia\nD) Asia")
        answer2 = input("\nEnter the letter to answer: ")
        if answer2 == "b" or answer2 == "B":
            print("Correct! Next question.")
            score += 1
        else:
            print("Incorrect! Next question.")

        print("\nWhich European country is famous for its boot-like shape on a map?\nA) Greece\nB) France\nC) Spain\nD) Italy")
        answer3 = input("\nEnter the letter to answer: ")
        if answer3 == "d" or answer3 == "D":
            print("Correct!")
            score += 1
            final_score()
        else:
            print("Incorrect!")
            final_score()
    
    #EXIT GAME
    elif action == "ESC" or action == "esc":
        quit()

    new_action = input("Do you want to continue the quiz with another topic?\nEnter Y to continue or N to exit the game: ")
    if new_action == "n" or new_action == "N":
        print("See you next time!")
        break
    else:
        score = 0
        continue

    
