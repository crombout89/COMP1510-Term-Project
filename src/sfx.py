import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

# Load background music
MAIN_GAME_MUSIC = "sfx/main-game-music.mp3"
SAD_ANIMAL_MUSIC = "sfx/sad-music-01.mp3"
FINALE_MUSIC = "sfx/finale-music.mp3"
HEAL_SFX = "sfx/cure-animal-sfx.mp3"

# Load sound effect
heal_sfx = pygame.mixer.Sound(HEAL_SFX)