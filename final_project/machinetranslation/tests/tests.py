import unittest, sys, os

sys.path.append(os.path.abspath(os.path.join('..', '.')))
from translator import english_to_french, french_to_english

class TestModules(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "")

if __name__ == "__main__":
    unittest.main()