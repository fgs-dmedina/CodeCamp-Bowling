from calculate_bowling_score import calculate_bowling_score

def test_all_misses_return_zero():
    assert calculate_bowling_score('--------------------') == 0

def test_all_ones_returns_twenty():
    assert calculate_bowling_score('11111111111111111111') == 20

def test_all_non_spares_returns_ninety():
    assert calculate_bowling_score('246813579-246813579-') == 90

def test_fives_with_spares_returns_one_fifty():
    assert calculate_bowling_score('5/5/5/5/5/5/5/5/5/5/5') == 150

def test_two_non_strikes_returns_two_eighty_five():
    assert calculate_bowling_score('XXXXXXXXXX5/') == 285

def test_tenth_frame_no_strike_returns_two_sixty_seven():
    assert calculate_bowling_score('XXXXXXXXX7/-') == 267

def test_all_strikes_returns_perfect_score():
    assert calculate_bowling_score('XXXXXXXXXXXX') == 300

def test_all_strikes_miss_last_frame_returns_two_forty():
    assert calculate_bowling_score('XXXXXXXXX--') == 240

def test_final_roll_as_strike_returns_two_seventy_nine():
    assert calculate_bowling_score('XXXXXXXXX9/X') == 279

def test_strikes_as_spares_returns_one_ten():
    assert calculate_bowling_score('X-/-/-/--X-/X--X--') == 110