import unittest
import RPS
from unittest.mock import patch


class Rock_Paper_Scissor(unittest.TestCase):

    
    def test_guess_rock(self):
        rock = ("Rock")
        convert_char = RPS.check_guess("r")
        self.assertEqual(convert_char,rock)
        convert_word = RPS.check_guess("ROCK")
        self.assertEqual(convert_word,rock)


    def test_guess_paper(self):
        rock = ("Paper")
        convert_char = RPS.check_guess("p")
        self.assertEqual(convert_char,rock)
        convert_word = RPS.check_guess("pApER")
        self.assertEqual(convert_word,rock)

    def test_guess_scissor(self):
        rock = ("Scissor")
        convert_char = RPS.check_guess("S")
        self.assertEqual(convert_char,rock)
        convert_word = RPS.check_guess("scissor")
        self.assertEqual(convert_word,rock)


if __name__ =='__main__':
    unittest.main()