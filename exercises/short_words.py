"""QZ02 Writing Function Practice: short_words."""
__author__ = "730668363"


def short_words(org_list: list[str]) -> list[str]:
    """Filters out the shorter words."""
    final_list: list[str] = []
    for words in org_list:
        if len(words) < 5:
            final_list.append(words)
        else:
            print(f"{words} is too long!")
    return final_list