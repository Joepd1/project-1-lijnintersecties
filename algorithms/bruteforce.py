# @author Joep Demollin
# @date 2022-11-04

from general import calculateIntersection

""" This function calculates all intersections (as Point objects) of the given list of edges.
    |param  edges An array of Edge objects.
    |return An array of Point objects.
"""
def bruteforce(edges):
    intersections = []
    n = len(edges)

    # Check if every combination of edges againts eachother for intersections
    for i in range(n):
        for j in range(i+1,n):
            newIntersect = calculateIntersection(edges[i], edges[j])
            if newIntersect : 
                intersections.append(newIntersect)
    return intersections