from unittest import TestCase
from translator import french_to_english, english_to_french

class TestIBMTranslator(TestCase):
    def test_null_input(self):
        self.assertIsNone(english_to_french(''))
        self.assertIsNone(french_to_english(''))

    def test_translation(self):
        self.assertEqual(
            english_to_french('Hello'),
            'Bonjour'
        )
        self.assertEqual(
            french_to_english('Bonjour'),
            'Hello'
        )