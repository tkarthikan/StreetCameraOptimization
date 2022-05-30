# a "Weber Street" (2,1) (2,2) (5,5) (5,6) (3,8)
# a "King Street S" (4,2) (4,8)
# a "Davenport Road" (1,4) (5,8)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(self.x, self.y)

class Street:
    def __init__(self, name="Name", points=[]):
        self.name = name
        self.points = []
        for p in points:
            self.points.append(Point(x=p[0], y=p[1]))

class Streets:
    def __init__(self):
        self.streets = []
        self.vertices = []

    def addStreet(self, name, points=[]):
        self.streets.append(Street(name=name, points=points))

    def print(self):
        for street in self.streets:
            print(street.name)
            for p in street.points:
                print(p.x, p.y)
    
    def printVertices(self):
        for v in self.vertices:
            print(v.x, v.y)

    def comparePoints(self, A, B):
        if (A.x==B.x)and(A.y==B.y):
            print("True")
            return True
        else:
            return False

    def checkVertex(self, vlist, v):
        for vertex in vlist:
            if (self.comparePoints(vertex, v)):
                return False
        return True

    def get_intersection (self, A, B, C, D): #start end start end
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
            return Point(x,y)

    def checkIntersections(self):
        self.vertices.clear()
        for i in range(len(self.streets)):
            for j in range(len(self.streets)):
                if (i<j):
                    for k in range(len(self.streets[i].points)-1):
                        for h in range(len(self.streets[j].points)-1):
                            A = self.streets[i].points[k]
                            print("A,B: ")
                            A.print()
                            B = self.streets[i].points[k+1]
                            B.print()
                            print("C,D: ")
                            C = self.streets[j].points[h]
                            D = self.streets[j].points[h+1]
                            C.print()
                            D.print()
                            if (self.intersect(A,B,C,D)):
                                print("Intersection")
                                if (self.checkVertex(self.vertices, A)):
                                    print("A in")
                                    self.vertices.append(A)
                                if (self.checkVertex(self.vertices, B)):
                                    print("B in")
                                    self.vertices.append(B)
                                if (self.checkVertex(self.vertices, C)):
                                    print("C in")
                                    self.vertices.append(C)
                                if (self.checkVertex(self.vertices, D)):
                                    print("D in")
                                    self.vertices.append(D)
                                E = self.get_intersection(A,B,C,D)
                                if (self.checkVertex(self.vertices, E)):
                                    print("E in")
                                    self.vertices.append(E)
                                #A.print()

    def ccw(self,A,B,C):
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

    # Return true if line segments AB and CD intersect
    def intersect(self,A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)


