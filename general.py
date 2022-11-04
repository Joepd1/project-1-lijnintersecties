# @author Joep Demollin
# @date 2022-11-04

from random import random
from math import sqrt

import numpy

class Point:
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord

class Edge:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointA = pointB

class Event:
    def __init__(self,xcoord, ycoord, type, shape1, shape2=None):
        self.xcoord = xcoord
        self.ycoord = ycoord
        #Three types of events; 1=top 2=intersection 3=bottom
        self.type = type
        self.shape1 = shape1
        self.shape2 = shape2
    def __gt__(self, other):
        if self.ycoord > other.ycoord: return True
        elif self.ycoord == other.ycoord and self.xcoord < other.xcoord: return True
        elif self.ycoord == other.ycoord and self.xcoord == other.xcoord and self.type<other.type: return True
        else: return False

    def __eq__(self, other):
        return self is other

    def __str__(self):
        return f"X:{self.xcoord} Y:{self.ycoord} Type:{self.type}"

""" This function generates an array of lines, represented by Edge objects.
The array will always assume we are working in a rectangle.
The size of this rectangle can be adjusted with (x/y)(bottom/top)
    | param amount: Integer Amount of lines to be generated.
    | param xbottom, xtop, ybottom, ytop: Confines of generatable points.
    | return Array of Edge objects.
"""
def createLinesRandom(amount, xbottom = -10, xtop=10, ybottom=-10, ytop=10):
    xsize = xtop-xbottom
    ysize = ytop - ybottom
    lines = []
    for i in range(amount):
        x1 = random()*xsize
        y1 = random()*ysize
        
        x2 = random()*xsize
        y2 = random()*ysize
        lines.append(Edge(Point(x1,y1), Point(x2,y2)))
    return lines

def createLinesShort(amount, xsize, ysize, maxdistance):
    lines = []
    for i in range(amount):
        x1 = random()*xsize
        y1 = random()*ysize

        while(True):
            x2 = random()*xsize
            y2 = random()*ysize

            if(distance(Point(x1,y1),Point(x2,y2)) <= maxdistance):
                break
            
        lines.append(Edge(Point(x1,y1), Point(x2,y2)))
    return lines

def createLinesNormal(amount, centerx, centery, stddev):
    lines = []
    for i in range(amount):
        x1 = numpy.random.normal(centerx,stddev)
        y1 = numpy.random.normal(centery,stddev)

        x2 = numpy.random.normal(x1,stddev)
        y2 = numpy.random.normal(y1,stddev)
        lines.append(Edge(Point(x1,y1), Point(x2,y2)))
    return lines

""" This function calculates the intersection of two given edges.
    |param edge1 A given Edge object.
    |param edge2 A given Edge object.
    |return The intersection as a Point object, or null.
"""
def calculateIntersection(edge1, edge2):
    i = edge1.pointA.xcoord
    
    def rico(edge):
        xdif = edge.pointB.xcoord - edge.pointA.xcoord
        ydif = edge.pointB.ycoord - edge.pointB.ycoord
        return ydif/xdif

    def verticalDisplacement(edge):
        return edge.pointA.ycoord - (edge.pointA.xcoord * rico1)

    rico1 = rico(edge1)
    rico2 = rico(edge2)

    b1 = verticalDisplacement(edge1)
    b2 = verticalDisplacement(edge2)

    if(rico1 == rico2):
        if(b1 == b2):
            raise Exception("Edges coincide.")
        else:
            return None
    else:
        xvalue = (b2-b1)/(rico1-rico2)
        yvalue = rico1 * xvalue + b1
        return Point(xvalue,yvalue)

def distance(point1, point2):
    return sqrt( (point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)