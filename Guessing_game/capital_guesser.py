import random
import json
import time


def play_again():
    answer = input("Would you like to play again? (y/n)").lower()
    if answer == "y":
        play()
    else:
        print("Thanks for playing.")


def play():
    with open("total_attempts.txt", "r") as score_file:
        total_attempts = json.loads(score_file.read())

    correct_guesses = 0
    wrong_guesses = 0
    countries = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Serbia": "Belgrade", "Spain": "Madrid",
                 "Austria": "Vienna", "Hungary": "Budapest", "Italy": "Rome", "Belarus": "Minsk",
                 "Slovakia": "Bratislava", "Germany": "Berlin", "Portugal": "Lisbon", "Norway": "Oslo",
                 "Ireland": "Dublin", "Greece": "Athens"}
    for x in range(5):
        random_country = random.choice(list(countries))
        capital = input(f"What is the capital city of {random_country}: ").lower()

        if capital == countries[random_country].lower():
            print("Congratulations, you are correct!")
            correct_guesses += 1
            total_attempts.append({"Correct": correct_guesses, "Wrong": wrong_guesses})
            with open("total_attempts.txt", "w") as score_file:
                score_file.write(json.dumps(total_attempts))

        else:
            print("Sorry, that's wrong!")
            wrong_guesses += 1
            total_attempts.append({"Correct": correct_guesses, "Wrong": wrong_guesses})
            with open("total_attempts.txt", "w") as score_file:
                score_file.write(json.dumps(total_attempts))
    print("")
    print("Correct guesses: " + str(correct_guesses))
    print("Wrong guesses: " + str(wrong_guesses))
    print("")
    play_again()


play()
time.sleep(5)
