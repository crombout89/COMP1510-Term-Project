import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

# Load background music
main_game_music = "sfx/main-game-music.mp3"
sad_animal_music = "sfx/sad-music-01.mp3"
finale_music = "sfx/finale-music.mp3"

# Load sound effects
heal_sfx = pygame.mixer.Sound("sfx/cure-animal-sfx.mp3")