"""
Task graph representation through dictionary
"""

GRAPH = {
    1: [2],
    2: [1,6,7],
    3: [6,7],
    4: [6,8,9],
    5: [6],
    6: [2,3,4,5],
    7: [2,3],
    8: [4,9],
    9: [4,8],
}
