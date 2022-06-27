import re
import os
WORDS = set()
with open("test/scrabble_dict.txt", 'r', encoding='utf8') as scrabble_words:
    for line in scrabble_words.readlines():
        WORDS.add(line.strip().upper())
SCORES = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
    "*": 0,
}
MAX_OCCURRENCES = {
        "A": 9,
        "B": 2,
        "C": 2,
        "D": 4,
        "E": 12,
        "F": 2,
        "G": 3,
        "H": 2,
        "I": 9,
        "J": 1,
        "K": 1,
        "L": 4,
        "M": 2,
        "N": 6,
        "O": 8,
        "P": 2,
        "Q": 1,
        "R": 6,
        "S": 4,
        "T": 6,
        "U": 4,
        "V": 2,
        "W": 2,
        "X": 1,
        "Y": 4,
        "Z": 1,
        "*": 2,
    }


def get_best_plays(hand: list[str], pattern: str, restriction: bool, output_limit: int) -> None:
    """Take hand and pattern, check against all words, score words, and return scores."""
    potential_plays = []
    available_letters = list(hand) + [char for char in pattern if char.isalpha()]
    for word in WORDS:
        if (pattern and re.search(pattern, word) is None) or (restriction and any(word.count(c) > MAX_OCCURRENCES[c.upper()] for c in word)):
            continue
        if check_valid_word(word, hand, pattern):
            potential_plays.append(word)
    word_scores = score_words(potential_plays, available_letters)
    output_scores(word_scores, hand, pattern, output_limit)


def output_scores(scores, hand, pattern, limit):
    """Output scores."""
    if len(pattern) > 0:
        print(f"Hand: {hand}, Fitting pattern: {pattern}")
    else:
        print(f"Hand: {hand}")
    if len(scores) == 0:
        print("No words found.")
    else:
        score_keys = sorted(scores.keys(), reverse=True)
        if limit > 0:
            score_keys = score_keys[:limit]
        for score in score_keys:
            print(f"{score}: ", end="")
            for word in scores[score]:
                print(word, end=", ")
            print("\b\b ")  # clear trailing COMMA and add NEWLINE


def check_valid_word(word: str, hand: list[str], pattern: str) -> bool:
    """Take player hand and pattern and see if word can be formed."""
    wilds = hand.count("*")
    for char in set(word):
        if (w_c := word.count(char)) > (p_c := pattern.count(char)) + (h_c := hand.count(char)) + wilds:
            return False
        if w_c > p_c + h_c:
            wilds -= w_c - h_c
    return True


def get_player_letters() -> str:
    """Query player for hand and clean input."""
    letter_list = input("What letters do you have (* for wild)?\n").upper()
    player_hand = "".join(sorted(char for char in letter_list if char.isalpha())) + "*" * letter_list.count("*")
    return player_hand


def score_words(word_list: list[str], available_letters: list[str]) -> dict:
    """Take list of words, score them, sort by score, and display."""
    scores = {}
    for word in word_list:
        if len(word) == len(available_letters):
            word_score = 50
        else:
            word_score = 0
        for char in word:
            word_score += SCORES[char]
        if word_score not in scores:
            scores[word_score] = []
        scores[word_score].append(word)
    return scores


def get_search_pattern() -> str:
    """Query player for pattern."""
    return input("Input pattern to use with dots for spaces. (eg. s..er)\n").upper()


def clear_screen() -> None:
    """Clean up output for user interaction."""
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def main():
    """Initialize data and show interface loop."""
    player_letters = get_player_letters()
    search_pattern = ""
    restrict_occurrences = False
    output_limit = 5
    while True:
        clear_screen()
        menu = f"""
            What would you like to do?\n
            1) Change player letters. Currently \"{player_letters}\".\n
            2) Set pattern to match. Currently \"{search_pattern}\".\n
            3) Toggle letter occurrence restrictions. Currently {restrict_occurrences}.\n
            4) Set output limit. Currently {output_limit}.\n
            Q) Quit\n
            Enter) Get suggested plays\n
        """
        selection = input(menu)
        if selection.lower() == "q":
            break
        if selection == "1":
            player_letters = get_player_letters()
        elif selection == "2":
            search_pattern = get_search_pattern()
        elif selection == "3":
            print("Letter occurrence restriction is now:", (restrict_occurrences := restrict_occurrences is False))
        else:
            get_best_plays(player_letters, search_pattern, restrict_occurrences, output_limit)
            input("Press Enter to continue...")


if __name__ == '__main__':
    main()
