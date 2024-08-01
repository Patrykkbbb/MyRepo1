def win(win_game):
    return win_game in ["y","n"]
def test_main():
    assert win("y") is True
    assert win("n") is True
    assert win("q") is False
def limit_numbers(max_number,min_number):
    if max_number > 100:
        return False
    if min_number < 0:
        return False
    else:
        return True
def test_main():
    assert limit_numbers(99,25) is True
    assert limit_numbers(150,-3) is False
    assert limit_numbers(150,0) is False