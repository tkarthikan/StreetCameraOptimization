class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print(self.x, self.y)

def get_intersection (A, B, C, D): #start end start end
    ax = A.x
    ay = A.y
    bx = B.x
    by = B.y
    cx = C.x
    cy = C.y
    dx = D.x
    dy = D.y
    d = (ax-bx)*(cy-dy)-(ay-by)*(cx-dx)
    if d == 0:
        return None #they are parallel
    a = ax*by-ay*bx
    b = cx*dy-cy*dx
    x1 = (a*(cx-dx))
    x2 = (b*(ax-bx))
    x = x1/d - x2/d
    y = (a*(cy-dy) - b*(ay-by))/d
    if (x <= max(ax, bx) and x >= min(ax, bx)) and (x <= max(cx, dx) and x >= min(cx, dx)): #between start and end of both lines
        print(x)
        print(y)
        return x,y

A = Point(1,4)
B = Point(5,8)
C = Point(4,2)
D = Point(4,8)
get_intersection(A,B,C,D)
