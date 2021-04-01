import sys

import pygame

import MazeGenAlgorithm

import random

pygame.init()

windowDimensions = (500, 500)

bgColour = (8, 8, 8)

edges = []

openList = []

closedList = []

displayName = ("Random Maze Generation Version 0")

displaySurface = pygame.display.set_mode(windowDimensions)

pygame.display.set_caption(displayName)

running = True

nodeMatrix = MazeGenAlgorithm.generateMazeBase(windowDimensions, 10, edges,)

def drawNodes(nodeMat):

    matrix = nodeMat

    for x in matrix:

        for y in x:

            y.drawNode(displaySurface)

def randomPrimsAlgorithm():



    pass

def randEdge():

    mazeEdgeNode = random.choice(edges)

    mazeEdgeNode.setStart(True)

    mazeEdgeNode.setEState(False)

    edges.remove(mazeEdgeNode)

    return mazeEdgeNode

mazeStart = randEdge()

currentNode = mazeStart

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()

    displaySurface.fill(bgColour)

    drawNodes(nodeMatrix)
    
    pygame.display.flip()