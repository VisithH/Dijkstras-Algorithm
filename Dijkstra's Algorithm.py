graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 5, 'D': 10},
    'C': {'A': 2, 'B': 5, 'D': 3},
    'D': {'B': 10, 'C': 3}
}


def distanceCalculator(graph, startNode, endNode):
    unvisited = {}
    Nodes = list(graph.keys())

    # Creates the Null and infinity unvisited table
    for currentNode in Nodes:
        # print(currentNode)
        unvisited.update({currentNode: (float('inf'), 'None')})
    # print(unvisited)

    # To avoid confusion and readability seperated it from the above one
    for currentNode in sorted(unvisited, key=lambda node: unvisited[node][0]):
        nodeKeys = list(graph[currentNode].keys())  # If in A -> [B, C]
        # print(nodeKeys)
        for neighbor in nodeKeys:  # gives me B and c seperated
            # For the startingNode
            if list(graph)[0] == currentNode:
                unvisited.update({currentNode: (0, 'None')})
                # comparing current node value with its previous node value
                if graph[currentNode][neighbor] < unvisited[neighbor][0]:
                    newDistance = graph[currentNode][neighbor]
                    unvisited.update({neighbor: (newDistance, currentNode)})
                # print(unvisited)
            # Everything else
            if graph[currentNode][neighbor] + unvisited[currentNode][0] < unvisited[neighbor][0]:
                newDistance = graph[currentNode][neighbor] + unvisited[currentNode][0]
                unvisited.update({neighbor: (newDistance, currentNode)})
                # print(unvisited)

    finalDistance = unvisited[list(unvisited)[-1]][0]
    print(f'Shortest Distance from {startNode} to {endNode} is {finalDistance}')

    # Finds the path Nodes
    path = [endNode]
    previousNode = unvisited[endNode][1]
    path.append(previousNode)
    for i in range(len(list(unvisited))):
        # Checks if the previous node is not None
        if unvisited[previousNode][1] != 'None':
            x = unvisited[previousNode][1]
            path.append(x)
            previousNode = x

    pathCorrectWay = path[::-1]
    print(f'The Path is {pathCorrectWay}')


startNode = list(graph)[0]
endNode = list(graph)[-1]
# print(endNode)
distanceCalculator(graph, 'A', endNode)
x = list(graph['A'].keys())
