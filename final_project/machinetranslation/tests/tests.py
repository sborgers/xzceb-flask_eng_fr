import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour") # Test translation of hello

    def test2(self):
        self.assertEqual(englishToFrench(),"Aucun texte anglais fourni pour la traduction") # text for null input

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") # Test translation of Bonjour

    def test2(self):
        self.assertEqual(frenchToEnglish(),"No French text provided for translation") # Test for null input

unittest.main()