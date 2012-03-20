''' This script generates bitmap representation of regular polygons,
    taking the number of sides as input.

    The method used computes the coordinates of vertices of the n-sided
    polygon by inscribing the polygon on a circle of fixed radius.

    From these vertices, each edge of the polygon is added to a bitmap
    using Bresenham's Line algorithm.

    http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
'''

import math
from optparse import OptionParser

class Bitmap():
    def __init__(self, width = 40, height = 40):
        assert width > 0 and height > 0
        self.width = width
        self.height = height
        self.map = [[ -1 for w in range(width)] for h in range(height) ]

    def chardisplay(self):
        txt = [''.join('0' if bit==-1 else '1'
                       for bit in row)
               for row in self.map]
        print('\n'.join(reversed(txt)))
 
    def set(self, x, y):
        self.map[y][x] = 1
 
    def get(self, x, y):
	    return self.map[y][x]

    def line(self, x0, y0, x1, y1):
        # Bresenham's line algorithm to obtain a bit map
	# Credits: rosettacode
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                self.set(x, y)
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                self.set(x, y)
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy        
        self.set(x, y)

def getCoordinates( n, r = 20, theta=0 ):
    # n = number of vertices in the regular polygon
    # r = radius of the circumscribing circle, a small radius would mean low resolution
    # theta = angle by which the polygon is to be rotated. eg: alpha = 45
    # (x,y) is the center of the polygon
    x =  y = size/2
    coordinates = []
    for i in range( 0, n ):
        angle =  theta * math.pi + ( 2 * math.pi * i ) / n
        coordinates.append( ( int ( round( x + r * math.cos( angle ) ) ), 
                            int ( round( y + r * math.sin( angle ) ) ) ) )
    return coordinates

parser = OptionParser()
parser.add_option("-n", "--sides", dest="n", type=int, default=3,
                  help="number of sides in the polygon")
parser.add_option("-r", "--radius", type=int, dest="r", default=10, 
                  help="radius of circle into which the polygon is inscribed")
parser.add_option("-t", "--theta", type=float, dest="theta", default=0.0,
                  help="angle to rotate the polygon by (in degrees), for eg: 90")

(args,op) = parser.parse_args()

size = 3 * args.r
bitmap = Bitmap(size, size)
coordinates = getCoordinates( args.n, args.r, args.theta/180.0 )

sides = ()
for i in range( 0, args.n ):
    sidesList = list( sides )
    sidesList.append( coordinates[ i ]  + coordinates[ ( i + 1 ) % args.n ] )
    sides = tuple( sidesList )

for points in sides:
    bitmap.line(*points)

bitmap.chardisplay()
