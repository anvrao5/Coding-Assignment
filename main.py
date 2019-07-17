import json
import math

input_x = int(input("Enter origin X coordinate: "))
input_y = int(input("Enter origin Y coordinate: "))

def sortfunction(c):
    x = int(c["value"].split(",")[0])
    y = int(c["value"].split(",")[1])
    return math.sqrt(math.pow(x-input_x, 2) + math.pow(y-input_y, 2))

def getClosestCoordinatesFromFile():
    with open('coordinates.json', 'r') as f:
        array = json.load(f)
    array.sort(key=sortfunction)
    return array

print(getClosestCoordinatesFromFile())
