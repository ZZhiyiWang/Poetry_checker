import unittest
import poetry_functions

SMALL_PRONOUNCING_LIST = [
    'HOW  HH AW1',
    'NOW N AW1',
    'BROWN  B R AW1 N',
    'COW C AW1',
    'CHOWDER  CH AW1 D ER0',
    'SHOW  SH OW1',
    'TOWN T AW1 N',
    'TOUT T AW1 T',
    'THEMISTOCLES DH EH1 M AH0 S T OW1 K L IY0 Z',
    'THERMOPYLAE TH ER2 M AA1 P IH1 L AY1',
    'THE  DH AH0',
    'PELOPONESSIAN  P EH1 L OW1 P OW1  N IY2 ZH EH1 N',
    'WAR W AO1 R',
    'X IH0 K S',
    'SQUARED S K W EH1 R D',
    'Y W AY1',
    'WHY W AY1',
    'H2SO4 EY1 CH T UW1 EH2 S OW1 F AO1 R',
    'SOFTWOOD S AO1 F T W UH2 D',
    'ORBER AO1 R B ER0',
    'COOPERATIVE  K OW0 AA1 P ER0 EY2 T IH0 V',
    'ACCELERATING AE0 K S EH1 L ER0 EY2 T IH0 NG',
    'THINKING TH IH1 NG K IH0 NG',
    'SARONG S ER0 AO1 NG',
]

pronunciation_dict = {}
for w in SMALL_PRONOUNCING_LIST:
    w_list = w.split()
    pronunciation_dict[w_list[0]] = w_list[1:]


class TestCheckSyllableCounts(unittest.TestCase):

    def test_check_syllable_counts_one_line_poem(self):
        """ Test check_syllable_counts on a one line poem. """

        poem_lines = ['How now brown cow.']
        pattern = ([4], ['A'])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'one-line poem')
        
    # Place your unit test definitions after this line.
    
    def test_check_syllable_counts_one_line_poem_with_no_specified(self):
        """ Test check_syllable_counts on a one-line poem with no specified \
        number of syllable. """

        poem_lines = ['How now brown cow.']
        pattern = ([0], ['A'])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'one-line poem no specified')
        
    def test_check_syllable_counts_three_line_poem_with_no_specified(self):
        """ Test check_syllable_counts on a three-line poem with no specified \
        number of syllable. """

        poem_lines = ['How', 'now', 'brown cow.']
        pattern = ([0, 0, 0], ['A', 'A', 'A'])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'three-line poem no specified')
        
    def test_check_syllable_counts_three_line_poem_with_some_specified(self):
        """ Test check_syllable_counts on a three-line poem with some specified\
        number of syllable. """

        poem_lines = ['How', 'now', 'brown cow.']
        pattern = ([0, 1, 2], ['A', 'A', 'A'])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'three-line poem some specified')
        
    def test_check_syllable_counts_three_line_poem_with_all_specified(self):
        """ Test check_syllable_counts on a three-line poem with all specified \
        number of syllable. """

        poem_lines = ['How', 'now', 'brown cow.']
        pattern = ([1, 1, 2], ['A', 'A', 'A'])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'three-line poem all specified')

    def test_check_syllable_counts_empty_poem(self):
        """ Test check_syllable_counts on an empty poem. """

        poem_lines = []
        pattern = ([], [])
        actual = poetry_functions.check_syllable_counts(poem_lines, pattern,
                                                        pronunciation_dict)
        expected = []
        self.assertEqual(actual, expected, 'empty poem')


# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)