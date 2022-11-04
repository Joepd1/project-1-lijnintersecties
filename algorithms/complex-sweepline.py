def smartSweepline(n, circles):
    intersections = []
    eventQueue = getAVLTreeQueue(circles)
    status = sbbst()
    combinationsChecked = dict()
    
    while(eventQueue.getSize() != 0):
        currentEvent = eventQueue.kthlargest(1)
        if(currentEvent.type == 1):    #Top of a circle
            status.insert(currentEvent.shape1.SemiCircleL)
            if combinationsChecked.get(currentEvent.shape1.SemiCircleL) is None:
                combinationsChecked[currentEvent.shape1.SemiCircleL] = set()

            status.insert(currentEvent.shape1.SemiCircleR)
            if combinationsChecked.get(currentEvent.shape1.SemiCircleR) is None:
                combinationsChecked[currentEvent.shape1.SemiCircleR] = set()
            intersections += newIntersections(currentEvent.shape1.SemiCircleL, combinationsChecked, status, eventQueue)
            intersections += newIntersections(currentEvent.shape1.SemiCircleR, combinationsChecked, status, eventQueue)
        elif(currentEvent.type == 2):    #Intersection
            switch(currentEvent, status)
            intersections += newIntersections(currentEvent.shape1, combinationsChecked, status, eventQueue)
            intersections += newIntersections(currentEvent.shape2, combinationsChecked, status, eventQueue)
        elif(currentEvent.type == 3):    #Bottom of a circle
            status.delete(currentEvent.shape1.SemiCircleL)
            status.delete(currentEvent.shape1.SemiCircleR)
        eventQueue.delete(eventQueue.kthlargest(1))
    return intersections
