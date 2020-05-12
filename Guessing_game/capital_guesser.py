import random


def play():
    countries = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Serbia": "Belgrade", "Spain": "Madrid",
                 "Austria": "Vienna", "Hungary": "Budapest", "Italy": "Rome", "Belarus": "Minsk",
                 "Slovakia": "Bratislava", "Germany": "Berlin", "Portugal": "Lisbon", "Norway": "Oslo",
                 "Ireland": "Dublin", "Greece": "Athens"}

    random_country = random.choice(list(countries))
    capital = input(f"What is the capital city of {random_country}: ").lower()

    if capital == countries[random_country].lower():
        answer = input("Congratulations, you are correct! \nWould you like to play again? (y/n)").lower()
        if answer == "y":
            play()
        else:
            print("Thanks for playing")
    else:
        answer = input("Sorry, that's wrong! \nWould you like to play again? (y/n)").lower()
        if answer == "y":
            play()
        else:
            print("Thanks for playing.")


play()
