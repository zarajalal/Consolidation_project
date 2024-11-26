import random

def initialize_game():
    """I wrote the code below to be the setup for the game, which will define the target score to win (25) and ask players to enter their names, which can be a fun way to personalize the game for each round if a bigger group of players wants to take turns."""
    target_score = 25
    players = input("Enter player names separated by commas:").split(',')
    scores = {player: 0 for  player in players}
    return target_score, players, scores 

def roll_dice():
    """This function will roll three dice and will return each value rolled in a list."""
    return [random.randint(1, 6) for _ in range(3)]

def play_turn(player):
    """Here, f-strings will be used to concatenate the list of the values rolled to the name of the player. This will print: "[player name] rolled: [number rolled]." If 3 values match, it will be returned that the player has tupled out. If a number was rolled twice, that will be printed to the terminal and the user will be asked if they want to tre-roll the non-fixed number. """
    while True: 
        dice = roll_dice()
        print(f"{player} rolled: {dice}")

        if dice[0] == dice[1] == dice[2]:
            print("Tupled out! Zero points for this turn.")
            return 0
        
        elif dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]:
            # This will identify and print the number that was rolled twice so it can be assigned to the fixed number.
            if dice[0] == dice[1]:
                fixed_number = dice[0]
            elif dice[1] == dice[2]:
                fixed_number = dice[1]
            else:
                fixed_number = dice[0]

            print(f"Fixed dice: Number {fixed_number} was rolled twice.")

            while True:
                try: 
                    reroll = input("Do you want to reroll the non-fixed dice? (yes/no)").strip().lower()
                    if reroll == "yes":
                        non_fixed_indices = [i for i in range(3) if dice[i] != fixed_number]
                        for index in non_fixed_indices:
                            dice[index] = random.randint(1, 6)
                        print(f"{player} rerolled: {dice}")
                        if dice[0] == dice[1] == dice[2]:
                            print("Tupled out! Zero points for this turn.")
                            return 0
                    elif reroll == "no":
                        break
                    else: 
                        print("Invalid input. Please enter 'yes' or 'no'.") 
                except Exception as err: 
                    print(f"An error occurred: {err}")
                    continue 

            return sum(dice)
        
        else:
            try: 
                stop = input("Do you want to stop and score your current roll? (yes/no): ").strip().lower()
                if stop == "yes":
                    return sum(dice)
                elif stop == "no":
                    continue
                else:
                    raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
            except ValueError as valueerror:
                print(valueerror)

def play_game(target_score, players, scores):
    """This function keeps track of the players' scores and compares them to the target score set in the intialize_game function above. The return values are different based on whether the target score of 25 is reached or not. """
    current_player_index = 0
    while all(score < target_score for score in scores.values()):
        current_player = players[current_player_index]
        print(f"\n{current_player}'s score: {scores[current_player]}")
        points = play_turn(current_player)
        scores[current_player] += points
        print(f"{current_player}'s score: {scores[current_player]}")

        if scores[current_player] >= target_score:
            print(f"{current_player} wins!")
            break

        current_player_index = (current_player_index + 1) % len(players)

#This will be used to initialize the game, allowing the initialize_game funtion I wrote in the beginning to set the player names and initialize the scores. 
target_score, players, scores = initialize_game()

#This will start the game by taking in the max score, two different player names, and their scores as the parameters. 
play_game(target_score, players, scores)

