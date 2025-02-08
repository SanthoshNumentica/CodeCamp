import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # If not enough history, play randomly
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Detect common patterns in opponent's last moves
    last_five = "".join(opponent_history[-5:])

    # Counter specific bots based on known strategies
    if "RRRRR" in last_five or "PPPPP" in last_five or "SSSSS" in last_five:
        # Opponent repeats the same move, counter it
        counter = {"R": "P", "P": "S", "S": "R"}
        return counter[opponent_history[-1]]
    
    # Predict opponent's most frequent move
    move_counts = {"R": opponent_history.count("R"), 
                   "P": opponent_history.count("P"), 
                   "S": opponent_history.count("S")}
    most_common_move = max(move_counts, key=move_counts.get)

    # Counter the most common move
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[most_common_move]
