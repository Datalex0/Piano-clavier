'''
Faire flèche / Exécuter le fichier Python
'''


# import pygame
import pygame
from pygame.locals import *
# import fonction de reconnaissance des touches clavier
from msvcrt import getch

# Initialisation de pygame
pygame.init()
pygame.mixer.init()

# Chargement des sons
sons = {}
sons["do"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/1_DO.wav.wav")
sons["do#"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/2_DO#.wav")
sons["re"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/3_RE.wav")
sons["re#"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/4_RE#.wav")
sons["mi"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/5_MI.wav")
sons["fa"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/6_FA.wav")
sons["fa#"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/7_FA#.wav")
sons["sol"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/8_SOL.wav")
sons["sol#"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/9_SOL#.wav")
sons["la"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/10_LA.wav")
sons["la#"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/11_LA#.wav")
sons["si"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/12_SI.wav")

sons["do2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/21_DO2.wav.wav")
sons["do#2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/22_DO#2.wav")
sons["re2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/23_RE2.wav")
sons["re#2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/24_RE#2.wav")
sons["mi2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/25_MI2.wav")
sons["fa2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/26_FA2.wav")
sons["fa#2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/27_FA#2.wav")
sons["sol2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/28_SOL2.wav")
sons["sol#2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/29_SOL#2.wav")
sons["la2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/30_LA2.wav")
sons["la#2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/31_LA#2.wav")
sons["si2"] = pygame.mixer.Sound("C:/Users/murai/OneDrive/Documents/GitHub/Piano clavier/SRC/Notes/32_SI2.wav")

# Association des touches clavier
touches = {}
touches["q"] = 'do'
touches["z"] = 'do#'
touches["s"] = 're'
touches["e"] = 're#'
touches["d"] = 'mi'
touches["f"] = 'fa'
touches["t"] = 'fa#'
touches["g"] = 'sol'
touches["y"] = 'sol#'
touches["h"] = 'la'
touches["u"] = 'la#'
touches["j"] = 'si'

touches["w"] = 'do2'
touches["i"] = 'do2#'
touches["x"] = 're2'
touches["c"] = 'mi2'
touches["v"] = 'fa2'
touches["b"] = 'sol2'
touches["n"] = 'la2'
touches[","] = 'si2'


while True:
    #Reconnaître la clé saisie
    bytes_clavier = getch()
    #Convertir d'une chaîne d'octets en chaîne de caractères
    str_clavier = bytes_clavier.decode("utf-8")
    #Aligner la chaîne sur les lettres minuscules
    touche = str_clavier.lower()
    print("note :", touches[touche])
    #Émet un son lorsque la touche enfoncée est dans le dictionnaire
    if touche in touches:
        x = touches[touche]
        sons[x].play()
    #Appuyez sur < pour quitter
    elif touche == '<':
        break
    