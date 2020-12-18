# Playing an mp3 file

# importing PyGame
import pygame

# Initializing PyGame
pygame.init()

# Loading the song
pygame.mixer.music.load("ex021.mp3")

# Setting the volume
pygame.mixer.music.set_volume(1)

# Start playing the song
pygame.mixer.music.play()
pygame.event.wait(100)