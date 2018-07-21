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


# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


# Add your helper functions here.

def vowel_phoneme(phoneme):
    """ (str) -> bool

    Return true iff it is a vowel phoneme.

    >>> vowel_phoneme('EH1')
    True
    >>> vowel_phoneme('Y')
    False
    """
    
    if phoneme[-1] in '012':
        return True
    return False

def count_syllable(line, word_to_phonemes):
    """ (str, pronunciation dictionary) -> int
    
    Return the number of syllables in a line.
    
    >>> count_syllable('secondary', {'SECONDARY': ['S', 'EH1', 'K', 'AH0', 'N',
    ...                                            'D', 'EH2', 'R', 'IY0']})
    4
    >>> count_syllable('Daniel', {'DANIEL': ['D', 'AE1', 'N', 'Y', 'AH0', 'L']})
    2
    """
    
    num_of_syllable = 0
    line_list = line.split()
    for i in range(len(line_list)):
        for j in range(len(word_to_phonemes[clean_up(line_list[i])])):
            if vowel_phoneme(word_to_phonemes[clean_up(line_list[i])][j]) == True:
                num_of_syllable += 1
    return num_of_syllable

def do_rhyme(line1, line2, word_to_phonemes):
    """ (str, str, pronunciation dictionary) -> bool
    
    Return True iff two lines rhyme.
    
    >>> do_rhyme('THE', 'A', {'THE': ['DH', 'AH0'], 'A': ['AH0']})
    True
    >>> do_rhyme('ABSURD', 'ADJOURNS', {'ABSURD': ['AH0', 'B', 'S', 'ER1', 
    ...                                              'D'],
    ...                                   'ADJOURNS': ['AH0', 'JH', 'ER1', 'N',
    ...                                                'Z']})
    False
    """
    
    line1_list = line1.split()
    line2_list = line2.split()
    new1 = []
    new2 = []
    for item1 in line1_list:
        new1.extend(word_to_phonemes[clean_up(item1)])
    for item2 in line2_list:
        new2.extend(word_to_phonemes[clean_up(item2)])
    return last_phonemes(new1) == last_phonemes(new2)


def pattern_dictionary(poetry_pattern):
    """ (poetry pattern) -> dict of {str: list of int}
    
    Reture a dictionary where each key is a a letter and each value is the \
    list of indexes of that letter. 
    
    >>> pattern_dictionary(([1,2], ['A', 'A']))
    {'A': [0, 1]}
    >>> pattern_dictionary(([3, 4, 5], ['B', 'B', 'B']))
    {'B': [0, 1, 2]}
    """
    
    dictionary = {}
    for i in range(len(poetry_pattern[1])):
        if poetry_pattern[1][i] not in dictionary:
            dictionary[poetry_pattern[1][i]] = [i]
        else:
            dictionary[poetry_pattern[1][i]].append(i) 
    return dictionary
    

# ===================== Required Functions =====================

def get_poem_lines(poem):
    r""" (str) -> list of str

    Return the non-blank, non-empty lines of poem, with whitespace removed
    from the beginning and end of each line.

    >>> get_poem_lines('The first line leads off,\n\n\n'
    ... + 'With a gap before the next.\nThen the poem ends.\n')
    ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    """
    
    result = poem.split('\n')
    for item in result:
        if item == '':
            result.remove(item)
    if result[-1] == '':
        return result[: -1]
    else:
        return result
 
    


def count_vowel_phonemes(phonemes):
    """ (list of list of str) -> int

    Return the number of vowel phonemes in phonemes.

    >>> phonemes = [['N', 'OW1'], ['Y', 'EH1', 'S']]
    >>> count_vowel_phonemes(phonemes)
    2
    """
    
    num_of_vowels = 0
    for i in range(len(phonemes)):
        for j in range(len(phonemes[i])):
            if vowel_phoneme(phonemes[i][j]) == True:
                num_of_vowels += 1
    return num_of_vowels


def last_phonemes(phoneme_list):
    """ (list of str) -> list of str

    Return the last vowel phoneme and any subsequent consonant phoneme(s) from
    phoneme_list, in the same order as they appear in phoneme_list.

    >>> last_phonemes(['AE1', 'B', 'S', 'IH0', 'N', 'TH'])
    ['IH0', 'N', 'TH']
    >>> last_phonemes(['IH0', 'N'])
    ['IH0', 'N']
    """
    
    i = len(phoneme_list) - 1
    while i >= 0:
        if vowel_phoneme(phoneme_list[i]) == True:
            return phoneme_list[i:]
        i -= 1
    return []
    

def check_syllable_counts(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

    Precondition: len(poem_lines) == len(pattern[0])

    Return a list of lines from poem_lines that do not have the right number of
    syllables for the poetry pattern according to the pronunciation dictionary.
    If all lines have the right number of syllables, return the empty list.

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 5, 4], ['*', '*', '*'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'],
    ...                     'A': ['AH0'],
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'],
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_syllable_counts(poem_lines, pattern, word_to_phonemes)
    ['With a gap before the next.', 'Then the poem ends.']
    >>> poem_lines = ['The first line leads off,']
    >>> check_syllable_counts(poem_lines, ([0], ['*']), word_to_phonemes)
    []
    """
    
    new_list = []
    for i in range(len(poem_lines)):
        if pattern[0][i] != 0 and \
            count_syllable(poem_lines[i], word_to_phonemes) != pattern[0][i]:
            new_list.append(poem_lines[i])
    return new_list
        


def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
    r""" (list of str, poetry pattern, pronunciation dictionary)
                                                        -> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with
    each other but don't. If all lines rhyme as they should, return the empty
    list.

    >>> poem_lines = ['The first line leads off,',
    ...               'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'],
    ...                     'A': ['AH0'],
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'],
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> bad_lines = check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    >>> bad_lines.sort()
    >>> bad_lines
    [['The first line leads off,', 'Then the poem ends.']]
    """
    new_list = []
    for i in range(len(pattern[1])):
        inner_list = []
        x = poem_lines[(pattern_dictionary(pattern)[pattern[1][i]])[0]]
        for j in range(len(pattern_dictionary(pattern)[pattern[1][i]])):
            if do_rhyme(x, 
                        poem_lines[(pattern_dictionary(pattern)\
                                    [pattern[1][i]])[j]],
                        word_to_phonemes) == False:
                for k in range(len(pattern_dictionary(pattern)[pattern[1][i]])):
                    inner_list.append(poem_lines[pattern_dictionary(pattern)\
                                                 [pattern[1][i]][k]])
        if inner_list != [] and inner_list not in new_list:
            new_list.append(inner_list)
    return new_list
        
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
