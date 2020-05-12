class FootballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


print("Enter new football player for your club!")

name_first = input("First name: ")
name_last = input("Last name: ")
height = input("Height: ")
weight = input("Weight: ")
goals = input("Number of goals: ")
cards_yellow = input("Yellow cards to date: ")
cards_red = input("Red cards to date: ")

new_player = FootballPlayer(first_name=name_first, last_name=name_last, height_cm=float(height),
                            weight_kg=float(weight), goals=int(goals), yellow_cards=int(cards_yellow),
                            red_cards=int(cards_red))

with open("new_players.txt", "w") as football_file:
    football_file.write(str(new_player.__dict__))

print("New player entered!")
