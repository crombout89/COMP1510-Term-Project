DIRECTION_MAPPING = {
    # "Direction input": (Direction vector)
    "W": (0, -1),  # Decriment y coordinate to move up
    "A": (-1, 0),  # Decriment x coordinate to move left
    "S": (0, 1),  # Incriment y coordinate to move down
    "D": (1, 0)  # Incriment x coordinate to move right
}


def main():
    for direction in DIRECTION_MAPPING.items():
        print('''
        def test_direction_input_to_action_''' + direction[0].lower() + '''_upper_case(self):
            actual = direction_input_to_action("''' + direction[0] + '''")
            expected = {
                'Type': 'Move',
                'Data': ''' + str(direction[1]) + '''
            }
            self.assertEqual(expected, actual)
            
        def test_direction_input_to_action_''' + direction[0].lower() + '''_lower_case(self):
            actual = direction_input_to_action("''' + direction[0].lower() + '''")
            expected = {
                'Type': 'Move',
                'Data': ''' + str(direction[1]) + '''
            }
            self.assertEqual(expected, actual)''')


if __name__ == "__main__":
    main()
