import pygame
import MazeGenAlgorithm
import sys

pygame.init()

windowDimensions = (900, 600)
bgColour = (32, 32, 32)

displayName = ("Random Maze Generation Version 0")

displaySurface = pygame.display.set_mode(windowDimensions)
pygame.display.set_caption(displayName)
displaySurface.fill(bgColour)

pygame.display.flip()

running = True

nodeMatrix = []

MazeGenAlgorithm.generateMazeBase(windowDimensions, 10, nodeMatrix, displaySurface)

print(nodeMatrix)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



