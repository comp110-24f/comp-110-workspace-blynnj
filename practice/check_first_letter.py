def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


check_first_letter(word="happy", letter="h")
check_first_letter(word="happy", letter="s")
