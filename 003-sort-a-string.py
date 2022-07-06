
def sort_a_string(phrase: str):
    return sorted(phrase.split(' '), key=str.casefold)

print(sort_a_string("Race a Car"))