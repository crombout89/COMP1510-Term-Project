import pygame

# Load background music
MAIN_GAME_MUSIC = "assets/sfx/main-game-music.mp3"
SAD_ANIMAL_MUSIC = "assets/sfx/sad-music-01.mp3"
FINALE_MUSIC = "assets/sfx/finale-music.mp3"
HEAL_SFX = "assets/sfx/cured-animal-02.wav"


def sfx_setup():
    # Initialize Pygame Mixer
    pygame.mixer.init()


def play_main_game_music():
    """ Play the main game music in a loop. """
    pygame.mixer.music.load(MAIN_GAME_MUSIC)
    pygame.mixer.music.play(loops=-1)


def play_sad_animal_music():
    """ Play the sad animal music indefinitely. """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(SAD_ANIMAL_MUSIC)
    pygame.mixer.music.play(loops=-1)


def play_finale_music():
    """ Play the finale music indefinitely. """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(FINALE_MUSIC)
    pygame.mixer.music.play(loops=-1)


def play_heal_sfx():
    """ Play the healed animal sound effect. """
    pygame.mixer.music.stop()
    pygame.mixer.music.load(HEAL_SFX)
    pygame.mixer.music.play()


def stop_music():
    """ Stop any currently playing music. """
    pygame.mixer.music.stop()


def main():
    """
    Drive the program.

    This is for testing only to make sure the sounds work properly.
    """
    sfx_setup()
    play_main_game_music()
    input("Press Enter to play sad animal music...")
    play_sad_animal_music()
    input("Press Enter to play healing sound effect...")
    play_heal_sfx()
    input("Press Enter to play finale music...")
    play_finale_music()
    input("Press Enter to stop all music...")
    stop_music()


if __name__ == "__main__":
    main()
