def calculate_bowling_score(rolls: str) -> int:

    #  1.  Create our frame_score, game_score,
    # and perfect score.    
    frame_score = 0
    frame_count = 10
    game_score = 0
    perfect_score = 300

    # 2.  Edge case - did the player have a perfect game?
    did_player_have_perfect_game = rolls == 'XXXXXXXXXXXX'
    if did_player_have_perfect_game:
        return perfect_score

    # 3.  Start iteration over our rolls and frames.
    for i in range(0, len(rolls)):


        # 5.  Create booleans to handle 
        # letters and symbols.
        is_roll_strike = rolls[i] == 'X'
        is_roll_spare = rolls[i] == '/'
        is_roll_miss = rolls[i] == '-'

        if is_roll_miss:
            continue
        
        game_score += int(rolls[i])

    return game_score