sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]


def connect_strings(list_of_senteces):
    """Connects list of strings into one string"""
    full_string = ''
    for sentence in list_of_senteces:
        full_string += ' ' + sentence

    full_string = full_string.lower() + ' '

    return full_string


def create_dictionary_of_words(full_string):
    """Creates a dictionary of words and number of their occurrences in a string"""
    list_of_words = full_string.split()  # Creating list of all words.
    list_of_words = list(dict.fromkeys(list_of_words))  # Deleting duplicates from the list  of  all words.

    # Creating a dictionary of words and the number of  their occurrences.
    dictionary_of_words = dict()
    for word in list_of_words:
        word = ' ' + word + ' '
        number_of_occurrences = full_string.count(word)
        dictionary_of_words[word] = number_of_occurrences
    return dictionary_of_words


def top_three_words_v_1(list_of_strings):
    """Prints top three words from a list of strings"""
    full_string = connect_strings(list_of_strings)
    dictionary_of_words = create_dictionary_of_words(full_string)
    a = 0
    for word in sorted(dictionary_of_words, key=dictionary_of_words.get, reverse=True):
        print(str(a + 1) + '. "' + word.strip() + '" - ' + str(dictionary_of_words[word]))
        a += 1
        if a == 3:
            break


def top_three_words_v_2(list_of_strings):
    """Prints top three words from a list of strings version 2: Cheat Edition"""
    from collections import defaultdict

    full_string = connect_strings(list_of_strings)

    dictionary_of_words = defaultdict(int)
    for w in full_string.split():
        dictionary_of_words[w] += 1
    a = 0
    for word in sorted(dictionary_of_words, key=dictionary_of_words.get, reverse=True):
        print(str(a + 1) + '. "' + word.strip() + '" - ' + str(dictionary_of_words[word]))
        a += 1
        if a == 3:
            break


if __name__ == '__main__':
    top_three_words_v_1(list_of_strings=sentences)
    print()
    top_three_words_v_2(list_of_strings=sentences)
