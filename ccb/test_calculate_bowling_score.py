from calculate_bowling_score import calculate_bowling_score

def test_all_misses_return_zero():
    assert calculate_bowling_score('--------------------') == 0

def test_all_ones_returns_twenty():
    assert calculate_bowling_score('11111111111111111111') == 20

def test_all_non_spares_returns_ninety():
    assert calculate_bowling_score('246813579-246813579-') == 90
