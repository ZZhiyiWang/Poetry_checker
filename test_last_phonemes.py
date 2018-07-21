import unittest
import poetry_functions


class TestLastPhonemes(unittest.TestCase):

    def test_last_phonemes_empty(self):
        """ Test last_phonemes on an empty list. """

        actual = poetry_functions.last_phonemes([])
        expected = []
        self.assertEqual(actual, expected, 'empty list')

    # Place your unit test definitions after this line.
    def test_last_phonemes_all_vowel_phonemes(self):
            """ Test last_phonemes on a list only contains vowel phonemes. """
    
            actual = poetry_functions.last_phonemes(['H1', 'CO2', 'TT0'])
            expected = ['TT0']
            self.assertEqual(actual, expected, 'all vowel phonemes') 
        
    def test_last_phonemes_no_vowel_phoneme(self):
            """ Test last_phonemes on a list without any vowel phonemes. """
        
            actual = poetry_functions.last_phonemes(['H', 'B', 'D'])
            expected = []
            self.assertEqual(actual, expected, 'no vowel phoneme')
    
    def test_last_phonemes_only_first_vowel_phoneme(self):
            """ Test last_phonemes on a list contains only one vowel phoneme \ 
            at index 0. """
                    
            actual = poetry_functions.last_phonemes(['H1', 'B', 'D'])
            expected = ['H1', 'B', 'D']
            self.assertEqual(actual, expected, 'only first vowel phoneme')
    
    def test_last_phonemes_only_middle_vowel_phoneme(self):
            """ Test last_phonemes on a list contains only one vowel phoneme \
            not at index 0 or index -1. """
                                
            actual = poetry_functions.last_phonemes(['H', 'B1', 'D'])
            expected = ['B1', 'D']
            self.assertEqual(actual, expected, 'only middle vowel phoneme') 
            
    def test_last_phonemes_only_last_vowel_phoneme(self):
            """ Test last_phonemes on a list contains only one vowel phoneme \
            at index -1. """
                                
            actual = poetry_functions.last_phonemes(['H', 'B', 'D1'])
            expected = ['D1']
            self.assertEqual(actual, expected, 'only last vowel phoneme')
            
    def test_last_phonemes_more_than_one_vowel_phonemes(self):
            """ Test last_phonemes on a list contains more than one vowel \
            phonemes, but not all."""
                                
            actual = poetry_functions.last_phonemes(['C', 'H1', 'A', 'N0', 'Y'])
            expected = ['N0', 'Y']
            self.assertEqual(actual, expected, 'more than one vowel phonemes') 
            
# Place your unit test definitions before this line.
if __name__ == '__main__':
    unittest.main(exit=False)
