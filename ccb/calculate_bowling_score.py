from convert_string_to_integer_list import convert_string_to_integer_list

def calculate_bowling_score(rolls: str) -> int:

    ALL_PINS = 10

    game_score = 0
    perfect_score = 300

    all_rolls = convert_string_to_integer_list(rolls)
    print(all_rolls)

    did_player_have_perfect_game = rolls == 'XXXXXXXXXXXX'
    if did_player_have_perfect_game:
        return perfect_score

    for i, roll in enumerate(rolls):
        pass



    print('Final game score: ' + str(game_score))
    return game_score

if __name__ == '__main__':
    calculate_bowling_score('5/5/5/5/5/5/5/5/5/5/5')
