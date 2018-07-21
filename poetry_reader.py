"""
A poetry pattern:  tuple of (list of int, list of str)
  o first item is a list of the number of syllables required in each line
  o second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  o each key is a word (a str)
  o each value is a list of phonemes for that word (a list of str)
"""

#helper functions:
def list_of_word(line):
    """ (str) -> list of str
    
    Return a list of string consisting every word in the line and deleting '\n'.
    
    >>> list_of_word('A AH0\n')
    ['A', 'AH0']
    >>> list_of_word('AA EY2 EY1\n')
    ['AA', 'EY2', 'EY1']
    """ 
    
    return line[:-1].split()


def get_list_of_nums(pattern_form):
    """ (list of str) -> list of int
    
    Return a list of integers which are the numbers of syllables in each line.
    
    >>> get_list_of_nums(['Haiku\n', '5 *\n', '7 *\n', '5 *\n', '\n'])
    [5, 7, 5]
    >>> get_list_of_nums(['Limerick\n', '8 A\n', '8 A\n', '5 B\n', '5 B\n', 
    ...                   '8 A\n', '\n'])
    [8, 8, 5, 5, 8]
    """
    
    num_list = []
    for item in pattern_form:
        if item[0].isdigit():
            num_list.append(int(item[0]))
    return num_list

def get_list_of_str(pattern_form):
    """ (list of str) -> list of str
    
    Return a list of string which are the rhyme scheme.
    
    >>> get_list_of_str(['Haiku\n', '5 *\n', '7 *\n', '5 *\n', '\n'])
    ['*', '*', '*']
    >>> get_list_of_str(['Limerick\n', '8 A\n', '8 A\n', '5 B\n', '5 B\n', 
    ...                   '8 A\n', '\n'])
    ['A', 'A', 'B', 'B', 'A']
    """
    
    str_list = []
    for item in pattern_form:
        if item[0].isdigit():
            str_list.extend(list_of_word(item)[1])
    return str_list




#required functions:

def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    
    r = pronunciation_file.readlines()
    pronunciation_dictionary = {}
    for i in range(len(r)):
        if r[i][0] != ';':
            lst = list_of_word(r[i])
            pronunciation_dictionary[lst[0]] = lst[1:]
    return pronunciation_dictionary
                
      

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    r = poetry_forms_file.readlines()
    poetry_pattern_dictionary = {}
    i = 0
    while i < len(r):
        if r[i][0].isalpha():
            j = i + 1
            new_list = []
            while j < len(r) and r[j] != '\n':
                new_list.append(r[j])
                poetry_pattern_dictionary[r[i][:-1]] = \
                    (get_list_of_nums(new_list), 
                     get_list_of_str(new_list))
                j += 1
        i += 1
    return poetry_pattern_dictionary
    
    
    

