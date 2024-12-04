import unittest
from src.character import start_final_challenge

class TestStartFinalChallenge(unittest.TestCase):

    def setUp(self):
        self.valid_character = {
            "InTree": True,
            "GroundCoordinates": (5, 5),
            "FinalChallengeCompleted": True
        }

if __name__ == '__main__':
    unittest.main()
