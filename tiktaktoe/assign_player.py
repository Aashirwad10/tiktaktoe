def pick_player():
    player=input("Enter Your Player: X or O")
    if player in ['X','O']:
        return player
    else:
        raise ValueError("Please Provide X or O")
