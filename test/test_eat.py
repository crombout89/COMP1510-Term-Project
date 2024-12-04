import io
import unittest
from unittest import TestCase
from unittest.mock import patch

from src.action import eat


class TestEat(TestCase):
    def test_eat_eat_silvervine_when_character_has_silvervine_return_value(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 1,
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        actual = eat(example_character, example_item)
        expected = True
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_silvervine_inventory_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 1,
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Inventory"]["Silvervine"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_silvervine_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 1,
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 100
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_silvervine_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 1,
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 50
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_silvervine_when_character_has_silvervine_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 1,
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🍽️ You ate a Silvervine.\n ⚡ Your Tummy is now at 100 and you have 50 extra energy.\n"
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_no_silvervine_return_value(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        actual = eat(example_character, example_item)
        expected = False
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_no_silvervine_inventory_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Inventory"]["Silvervine"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_no_silvervine_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_silvervine_when_character_has_no_silvervine_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_silvervine_when_character_has_no_silvervine_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Silvervine": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Silvervine",
            "Data": None
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🚫 You can't eat this item because it's not in your inventory!\n"
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_catnip_return_value(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        actual = eat(example_character, example_item)
        expected = True
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_catnip_inventory_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Inventory"]["Catnip"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_catnip_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 50
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_catnip_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 25
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_catnip_when_character_has_catnip_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🍽️ You ate a Catnip.\n ⚡ Your Tummy is now at 50 and you have 25 extra energy.\n"
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_no_catnip_return_value(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        actual = eat(example_character, example_item)
        expected = False
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_no_catnip_inventory_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Inventory"]["Catnip"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_no_catnip_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_catnip_when_character_has_no_catnip_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 0,
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_catnip_when_character_has_no_catnip_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 0
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Catnip",
            "Data": None
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🚫 You can't eat this item because it's not in your inventory!\n"
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_berry_return_value(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        actual = eat(example_character, example_item)
        expected = True
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_berry_inventory_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = example_character["Inventory"]["Berries"]["Red"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_berry_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 25
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_berry_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_berry_when_character_has_berry_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🍽️ You ate a Red Berry.\n ⚡ Your Tummy is now at 25 and you have 0 extra energy.\n"
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_no_berry_return_value(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 0
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        actual = eat(example_character, example_item)
        expected = False
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_no_berry_inventory_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 0
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = example_character["Inventory"]["Berries"]["Red"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_no_berry_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 0
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_berry_when_character_has_no_berry_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 0
                },
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_berry_when_character_has_no_berry_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Berries": {
                    "Red": 0
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "Berry",
            "Data": "Red"
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🚫 You can't eat this item because it's not in your inventory!\n"
        self.assertEqual(expected, actual)

    def test_eat_eat_nonexistant_item_tummy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1,
                "SilverVine": 1,
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "ReesesCup",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["Tummy"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_eat_eat_nonexistant_item_extra_energy_change(self):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1,
                "SilverVine": 1,
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "ReesesCup",
            "Data": None
        }
        eat(example_character, example_item)
        actual = example_character["ExtraEnergy"]
        expected = 0
        self.assertEqual(expected, actual)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_eat_eat_nonexistant_item_console_output(self, mock_output):
        example_character = {
            "Tummy": 0,
            "ExtraEnergy": 0,
            "Inventory": {
                "Catnip": 1,
                "SilverVine": 1,
                "Berries": {
                    "Red": 1
                }
            }
        }
        example_item = {
            "Type": "Item",
            "Name": "ReesesCup",
            "Data": None
        }
        eat(example_character, example_item)
        actual = mock_output.getvalue()
        expected = "🚫 You can't eat this item because it's not in your inventory!\n"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
