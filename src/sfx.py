import pygame

# Initialize Pygame Mixer
pygame.mixer.init()

# Load background music
MAIN_GAME_MUSIC = "../sfx/main-game-music.mp3"
SAD_ANIMAL_MUSIC = "../sfx/sad-music-01.mp3"
FINALE_MUSIC = "../sfx/finale-music.mp3"
HEAL_SFX = "../sfx/cure-animal-sfx.mp3"

# Load sound effect
animal_healed_sfx = pygame.mixer.Sound(HEAL_SFX)

# Functions to control music and SFX
def play_main_game_music():
    """ Play the main game music in a loop. """
    pygame.mixer.music.load(MAIN_GAME_MUSIC)
    pygame.mixer.music.play(loops=-1)

def play_sad_animal_music():
    """ Play the sad animal music once. """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(SAD_ANIMAL_MUSIC)
    pygame.mixer.music.play()

def play_finale_music():
    """ Play the finale music indefinitely. """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(FINALE_MUSIC)
    pygame.mixer.music.play(loops=-1)

def play_heal_sfx():
    """ Play the healed animal sound effect. """
    pygame.mixer.music.stop()
    pygame.time.delay(800)
    animal_healed_sfx.play()

def stop_music():
    """ Stop any currently playing music. """
    pygame.mixer.music.stop()

def set_music_volume(volume):
    """ Set the volume for the background music (0.0 to 1.0). """
    pygame.mixer.music.set_volume(volume)

def set_sfx_volume(volume):
    """ Set the volume for the sfx music (0.0 to 1.0). """
    animal_healed_sfx.set_volume(volume)

if __name__ == "__main__":
    play_main_game_music()
    input("Press Enter to play sad animal music...")
    play_sad_animal_music()
    input("Press Enter to play healing sound effect...")
    play_heal_sfx()
    input("Press Enter to play finale music...")
    play_finale_music()
    input("Press Enter to stop all music...")
    stop_music()