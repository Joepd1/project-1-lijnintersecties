# @author Joep Demollin
# @date 2022-11-04

from general import Edge, Point, createRandomLines

def createInput(nbLines, maxRadius = None, upperXLimit = 5, upperYLimit = 5, lowerXLimit = -5, lowerYLimit = -5):
    with open('input.txt', 'w') as f:
        #f.write(f"{math.floor(random.randrange(0,2))+1}\n")
        #f.write(f"3\n")
        f.write(f"{nbLines}\n")
        lines = createRandomLines(nbLines)
        for i in lines:
            f.write(f"{i.pointA.xcoord} {i.pointA.ycoord} {i.pointB.xcoord} {i.pointB.ycoord}\n")

def readInput():
    edges = []
    with open('input.txt') as i:
        lines = i.readlines()
    
    n = int(lines[0])
    
    for line in lines:
        x = line.split()
        edges.append( Edge( Point(x[0],x[1]), Point(x[2],x[3])))

    return edges

def writeOutput(intersections):
    with open('output.txt', 'w') as f:
        for i in intersections:
            f.write(f"{i.xcoord} {i.ycoord}\n")