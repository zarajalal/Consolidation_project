import random

def initialize_game():
    """I wrote the code below to be the setup for the game, which will define the target score to win (25) and ask players to enter their names, which can be a fun way to personalize the game for each round if a bigger group of players wants to take turns."""
    target_score = 25
    players = input("Enter player names separated by commas, do not add spaces:").split(',')
    players = [player.strip() for player in players] 
    scores = {player: 0 for  player in players}
    return target_score, players, scores 

def roll_dice():
    """This function will roll three dice and will return each value rolled in a list."""
    return [random.randint(1, 6) for _ in range(3)]

def play_turn(player):
    """Here, [insert functionality when finished with while/else loop; ok for now]"""
    while True: 
        dice = roll_dice()
        print(f"{player} rolled: {dice}")

        if dice[0] == dice[1] == dice[2]:
            print("Tupled out! Zero points for this turn.")
            return 0
        
        elif dice[0] == dice[1] or dice[1] == dice[2] or dice[0] == dice[2]:
            # 
            if dice[0] == dice[1]:
                fixed_number = dice[0]
            elif dice[1] == dice[2]:
                fixed_number = dice[1]
            else:
                fixed_number = dice[0]

            print(f"Fixed dice: Number {fixed_number} was rolled twice.")

            while True:
                try: 
                    reroll = input("Do you uwant to reroll the non-fixed dice? (yes/no)").strip().lower()
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
                except Exception as e: 
                    print(f"An error occurred: {e}")
                    continue 

            return sum(dice)
        
        else:
            # could have try, if, elif, else? them at end can except value error and then print it 

def play_game(target_score, players, scores):
# function can keep trac of scores, set an index to zero and print each players score

#add more here to set up start of game when program is run; should be enough to run according to rules. check when done