# @author Joep Demollin
# @date 2022-11-04

from general import calculateIntersection

"""

"""
def simpleSweepline(lines):
    Q = getSimpleQueue(lines)
    status = []
    intersections = []

    for event in Q:
        if event.type == 1:
            status.append(event.shape1)
            for active in status:
                # For all elements of the status not equal to element just added
                if not active is event.shape1:
                    # Add 
                    intersections += calculateIntersection(event.shape1, active)

        if event.type == 3:
            status.remove(event.shape1)
    return intersections

"""

"""
def getSimpleQueue(circles):
    Q = list()
    for circle in circles:
        Q.append( Event(circle.xcoord, circle.ycoord+circle.radius, 1, circle))
        Q.append( Event(circle.xcoord, circle.ycoord-circle.radius, 3, circle))
    Q.sort(reverse=True)
    return Q