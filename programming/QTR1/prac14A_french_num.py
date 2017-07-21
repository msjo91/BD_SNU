"""
Translate 0 to 100 in French.
"""


def digit(num, pos):
    return num // 10 ** (pos - 1) % 10


def num_in_french(num):
    ones_list = [
        "zero", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf",
        "dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"
    ]
    tens_list = ["", "dix", "vingt", "trente", "quarante",
                 "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]

    if 0 <= num < 20:
        return ones_list[num]

    elif 20 <= num < 70:
        if digit(num, 1) == 0:
            return tens_list[digit(num, 2)]
        elif digit(num, 1) == 1:
            return tens_list[digit(num, 2)] + " et " + ones_list[1]
        else:
            return tens_list[digit(num, 2)] + "-" + ones_list[digit(num, 1)]

    elif digit(num, 2) == 7 or digit(num, 2) == 9:
        if digit(num, 1) == 1:
            return tens_list[digit(num, 2)] + " et " + ones_list[11]
        elif digit(num, 1) < 7:
            return tens_list[digit(num, 2)] + "-" + ones_list[digit(num, 1) + 10]
        else:
            return tens_list[digit(num, 2)] + "-" + tens_list[1] + "-" + ones_list[digit(num, 1)]

    elif 80 <= num < 90:
        if num == 80:
            return tens_list[8] + "s"
        else:
            return tens_list[8] + "-" + ones_list[digit(num, 1)]

    elif num == 100:
        return "cent"


def print_french(lo, hi):
    print(*[num_in_french(i) for i in range(lo, hi + 1)])
