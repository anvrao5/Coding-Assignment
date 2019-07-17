import json 
import math 

class CoordinateSortComparator:
    def __init__(self, originX, originY):
        self.originX = originX
        self.originY = originY

    # custom sort comparator
    def sortfunction(self, c):
        x = int(c["value"].split(",")[0])
        y = int(c["value"].split(",")[1])
        return math.sqrt(math.pow(x-self.originX, 2) + math.pow(y-self.originY, 2))

# function which returns the sorted closest corordinates
def getClosestCoordinatesFromFile(x, y):
    # open and read file
    with open('coordinates.json', 'r') as f:
        array = json.load(f)
    # init comparator class
    customSort = CoordinateSortComparator(x, y)
    # sort
    array.sort(key=customSort.sortfunction)
    return array

# Example console input
input_x = int(input("Enter origin X coordinate: "))
input_y = int(input("Enter origin Y coordinate: "))

print(getClosestCoordinatesFromFile(input_x, input_y))
