from node import *
from math import *

def nodeInList(list, targetNode):
    for node in list:
        if (targetNode == node):
            return True
    return False

def findIndexOfNode(list, targetNode):
    for node in list:
        if (targetNode == node):
            return list.index(node)

def astar(start, target, maze):
    # Initialize nodes
    startNode = Node(None, start)
    targetNode = Node(None, target)

    openList = []
    closedList = []

    openList.append(startNode)

    while openList:
        # sort openList by f and then move the least cost node to closedList
        openList.sort(key=lambda x: x.f)
        currNode = openList[0]
        closedList.append(currNode)
        openList.remove(currNode)

        # Stop when you add the target to the closed list
        if (currNode == targetNode):
            path = []

            # Construct the path
            while (currNode):
                path.append(currNode.position)
                currNode = currNode.parent
            path.reverse()
            
            return path

        # Generate the children of the current node
        children = []
        children.append(Node(currNode, (0,0)))
        for new_position in [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]:
            node_position = (new_position[0] + currNode.position[0], new_position[1] + currNode.position[1])

            # Verify that the child is a valid node
            if ((node_position[0] > -1) and (node_position[0] < len(maze))
                and (node_position[1] > -1) and (node_position[1] < len(maze[0]))):

                # Verify that the child is a walkable node
                if (maze[node_position[0]][node_position[1]] == 0):
                    childNode = Node(currNode, node_position)
                    children.append(childNode)
        
        for child in children:
            # Verify that the child has not yet been explored
            if (nodeInList(closedList, child)):
                continue

            child.g = child.parent.g + 1
            child.h = sqrt((child.position[0] - targetNode.position[0])**2 + (child.position[1] - targetNode.position[1])**2)
            child.f = child.g + child.h

            if (not nodeInList(openList, child)):
                # Add the child to the open list if it isn't already in it
                openList.append(child)
            else:
                # Update the child if it's already in the list and if it can be optimized
                index = findIndexOfNode(openList, child)
                if (openList[index].g > child.g):
                    openList[index].g = child.g
                    openList[index].f = child.f
                    openList[index].parent = currNode

def printSolution(path, maze):
    if (path):
        # Add the path to the maze
        for step in path:
            maze[step[0]][step[1]] = 2
        
        # Display the maze in a nicer way
        for row in maze:
            for space in row:
                if (space == 0):
                    print(". ", end="")
                elif (space == 1):
                    print("# ", end="")
                else:
                    print("o ", end="")
            print("")

    else:
        print("There is no path")
    