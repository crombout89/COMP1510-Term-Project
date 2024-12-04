import unittest
from src.entity import generate_animal
from src.config import ANIMAL_OPTIONS

class TestGenerateAnimal(unittest.TestCase):

    def setUp(self):
        self.character = {"Level": 3}

    def test_animal_generation(self):
        animal = generate_animal(self.character)

        # Check the type and name of the animal
        self.assertEqual(animal["Type"], "Animal")
        self.assertIn(animal["Name"], ANIMAL_OPTIONS)

        # Check the number of ailments
        self.assertGreaterEqual(len(animal["Data"]), 1)
        self.assertLessEqual(len(animal["Data"]), self.character["Level"])

    def test_unique_ailments(self):
        animal = generate_animal(self.character)
        self.assertEqual(len(animal["Data"]), len(set(animal["Data"])))

    def test_ailments_count(self):
        for level in range(1, 4):  # Test levels from 1 to 3
            self.character["Level"] = level
            animal = generate_animal(self.character)
            self.assertGreaterEqual(len(animal["Data"]), 1)
            self.assertLessEqual(len(animal["Data"]), level)

if __name__ == '__main__':
    unittest.main()
