from QTR1.random_PRNG import prng


def roll_dice():
    roll = prng() % 6 + 1
    assert 1 <= roll <= 6
    return roll


def election_year():
    election_number = prng() % ((2017 - 1788) // 4 + 1)
    assert 0 <= election_number <= 56
    year = election_number * 4 + 1788
    assert 1788 <= year <= 2017 and year % 4 == 0
    return year
