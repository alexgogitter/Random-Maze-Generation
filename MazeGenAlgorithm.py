##Maze Generation

print("importing Maze Generation Version 0")


class node:
    def __init__(self, position):
        self.parent = None
        self.position = position
        self.traversed = False
        self.nodeDimension = 8
        traversableCol = (255, 255, 255)
        nonTraversableCol = (64, 64, 64)

    def draw(screen):
        if traversed:
            pygame.draw.rect(screen, traversableCol, (position[0], position[1], 8, 8), 0)
        else:
            pygame.draw.rect(screen, nonTraversableCol, (position[0], position[1], 8, 8), 0)





def generateMazeBase(windowDimensions, nodeWidth, nodeMatrix, screen,):
    navWidth = windowDimensions[0]//nodeWidth
    navHeight = windowDimensions[1]//nodeWidth

    xList = []
    yList = []

    for xNode in range(0, (navWidth + 1), 1):
        for yNode in range(0, (navHeight + 1), 1):
            position = [xNode, yNode]
            Node = node(position)
            xList.append(Node)

        xList.append(list(yList))
        yList.clear

    nodeMatrix.append(list(xList))





