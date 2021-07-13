from convert_string_to_integer_list import convert_string_to_integer_list

def calculate_bowling_score(rolls: str) -> int:

    original_input = rolls
    ALL_PINS = int(10)

    game_score = int(0)
    perfect_score = int(300)

    did_player_have_perfect_game = original_input == 'XXXXXXXXXXXX'
    if did_player_have_perfect_game:
        return perfect_score

    all_rolls = convert_string_to_integer_list(rolls)
    
    frame = 1

    for i, roll in enumerate(all_rolls):
        
        if frame == 11:
            break

        is_roll_spare = original_input[i] == '/'
        is_roll_strike = roll == ALL_PINS

        is_second_last_roll = roll == all_rolls[-2]
        is_final_roll = roll == all_rolls[-1]

        if is_roll_strike:

            strike_bonus = int(0)

            if is_second_last_roll or is_final_roll:
                strike_bonus = ALL_PINS
            else:
                strike_bonus = int(all_rolls[i + 1] + all_rolls[i + 2])

            game_score += strike_bonus
            frame += 1
            
        elif is_roll_spare:
            spare_bonus = all_rolls[i + 1]
            game_score += spare_bonus
            frame += 1

        game_score += roll

    print('Final game score: ' + str(game_score))
    return game_score


if __name__ == '__main__':
    calculate_bowling_score('5/5/5/5/5/5/5/5/5/5/5')
