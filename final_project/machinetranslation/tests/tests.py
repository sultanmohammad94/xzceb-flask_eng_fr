from unittest import TestCase
from translator import french_to_english, english_to_french

class TestIBMTranslator(TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour').lower(), 'Hello'.lower())
        self.assertEqual(french_to_english('Bonsoir').lower(), 'Good evening'.lower())
        self.assertNotEqual(french_to_english('Bonjour').lower(), ' '.lower())
        
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello').lower(), 'Bonjour'.lower())
        self.assertEqual(english_to_french('Good evening').lower(), 'Bonsoir'.lower())
        self.assertNotEqual(english_to_french('Hello').lower(), ''.lower())
        
