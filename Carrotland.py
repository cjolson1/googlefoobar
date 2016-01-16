"""
Carrotland
==========

The rabbits are free at last, free from that horrible zombie science experiment. 
They need a happy, safe home, where they can recover. 

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! 
But first, you need some land. And the only person who's selling land is Farmer Frida. 
Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. 
However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: 
The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land 
and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two integers representing 
the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. 
The three vertices will not be collinear.

Test cases
==========

Inputs:
    (int) vertices = [[2, 3], [6, 9], [10, 160]]
Output:
    (int) 289

Inputs:
    (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
Output:
    (int) 1730960165
"""
from math import sqrt
from fractions import gcd



def area_calc(vertices):
    point0 = vertices[0]
    point1 = vertices[1]
    point2 = vertices[2]
    edges = {
        (0,1): sqrt((point1[0] - point0[0]) ** 2 + (point1[1] - point0[1]) ** 2),
        (0,2): sqrt((point2[0] - point0[0]) ** 2 + (point2[1] - point0[1]) ** 2),
        (1,2): sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2),
    }
    # Heron's Formula
    s = float(sum(edges.values())) / 2
    a = edges.values()[0]
    b = edges.values()[1]
    c = edges.values()[2]
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area
    

def boundary_calc(vertices):
    boundary_points = 0
    point0 = vertices[0]
    point1 = vertices[1]
    point2 = vertices[2]
    # number of lattice points on each line is equivalent to gcd(x,y)+1 when taken from (0,0) to (x,y)
    xy01 = (abs(point1[0] - point0[0]), abs(point1[1] - point0[1]))
    xy02 = (abs(point2[0] - point0[0]), abs(point2[1] - point0[1]))
    xy12 = (abs(point2[0] - point1[0]), abs(point2[1] - point1[1]))
    boundary_points += gcd(xy01[0], xy01[1])
    boundary_points += gcd(xy02[0], xy02[1])
    boundary_points += gcd(xy12[0], xy12[1])
    return boundary_points
    
    
def answer(vertices):
    # basically going to utilize Pick's Theorem to find the number of interior points
    # area = B/2 + I - 1
    area = area_calc(vertices)
    boundary_points = boundary_calc(vertices)
    # if the area is 0, a.k.a. all points are the same, the number of carrots that can be planted is 0.
    if area == 0:
        return 0
    carrots = area - float(boundary_points) / 2 + 1
    # for some reason when trying to convert carrots from a float to an int,
    # it will subtract one from the value. So you gotta use the round functionality.
    # e.g. 289.0 -> 288
    return int(round(carrots))
