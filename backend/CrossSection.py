import math

class shape(object):
    def __init__(self):
        pass

class square(shape):
    def __init__(self, point1, point2): #coordinates in list [[x1, y1],[x2,y2]]
        self._x1 = point1[0]
        self._y1 = point1[1]
        self._x2 = point2[0]
        self._y2 = point2[1]

    def get_area(self): # A
    	return abs((self._x2-self._x1)*(self._y2-self._y1))

    def get_centroid_origin(self): # y
    	return [(self._x2+self._x1)/2, (self._y2+self._y1)/2]

    def get_first_moment_area(self):
        return (self.get_area()*self.get_centroid_origin()[0],self.get_area()*self.get_centroid_origin()[1])

    def get_moment_of_inertia(self):
        Ix = (1/12)*abs(self._x2-self._x1)*math.pow(abs(self._y2-self._y1),3)
        Iy = (1/12)*abs(self._y2-self._y1)*math.pow(abs(self._x2-self._x1),3)
        return (Ix,Iy)




class cross_section:
    def __init__(self, shapes):
        self._shapes = shapes

    def get_total_area(self):
        total_A = 0
        for i in self._shapes:
            total_A += i.get_area()
        return total_A

    def get_first_moment_area(self):
        first_moment_area_x = 0
        first_moment_area_y = 0

        for i in self._shapes:
            first_moment_area_x += i.get_first_moment_area()[0]
            first_moment_area_y += i.get_first_moment_area()[1]
        return (first_moment_area_x, first_moment_area_y)

    def get_centroid_origin(self):
        return (self.get_first_moment_area()[0]/self.get_total_area(),self.get_first_moment_area()[1]/self.get_total_area())






if __name__ == '__main__':

    item1 = square([6,17],[18,15])
    item2 = square([11.5,15],[12.5,5])
    section = cross_section([item1, item2])

    for item in section._shapes:
        print('Area of item is: '+str(item.get_area()))
        print('Centroid of item towards origin: '+str(item.get_centroid_origin()))
        print('First Moment of Area of item towards origin: '+str(item.get_first_moment_area()))
        print('Moment of Ineartia of item: '+str(item.get_moment_of_inertia()))
        print('')

    print(section.get_total_area())
    print(section.get_first_moment_area())
    print(section.get_centroid_origin())
