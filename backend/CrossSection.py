import math

class square:

    def __init__(self, point1, point2): #   Coordinates in list [[x1, y1],[x2,y2]]
        self._x1 = float(point1[0])
        self._y1 = float(point1[1])
        self._x2 = float(point2[0])
        self._y2 = float(point2[1])

    def get_points(self):
        return [(self._x1,self._y1),(self._x2,self._y2)]

    def get_area(self):
    	return abs((self._x2-self._x1)*(self._y2-self._y1))

    def get_centroid_origin(self):
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

    def get_second_moment_area(self):
        second_moment_area_x = 0
        second_moment_area_y = 0
        for i in self._shapes:
            second_moment_area_x += i.get_area()*math.pow(self.get_centroid_origin()[0]-i.get_centroid_origin()[0],2)
            second_moment_area_y += i.get_area()*math.pow(self.get_centroid_origin()[1]-i.get_centroid_origin()[1],2)
        return (second_moment_area_x, second_moment_area_y)

    def get_sum_moments_of_inertia(self):
        sum_x = 0
        sum_y = 0
        for i in self._shapes:
            sum_x += i.get_moment_of_inertia()[0]
            sum_y += i.get_moment_of_inertia()[1]
        return (sum_x, sum_y)

    def get_moments_of_inertia(self):   #   Carefull here - dont mix up the axes
        return(self.get_sum_moments_of_inertia()[0] + self.get_second_moment_area()[1], self.get_sum_moments_of_inertia()[1] + self.get_second_moment_area()[0])

    def get_furthest_point(self):

        z_max_distance = 0
        y_max_distance = 0

        for i in self._shapes:
            z_max = max(abs(i.get_points()[0][1]-self.get_centroid_origin()[1]),abs(i.get_points()[1][1]-self.get_centroid_origin()[1]))
            y_max = max(abs(i.get_points()[0][0]-self.get_centroid_origin()[0]),abs(i.get_points()[1][0]-self.get_centroid_origin()[0]))
            if z_max > z_max_distance:
                z_max_distance = z_max

            if y_max > y_max_distance:
                y_max_distance = y_max

        return (z_max_distance, y_max_distance)


    def get_section_modulus(self):

        z_max_distance = 0
        y_max_distance = 0

        for i in self._shapes:
            z_max = max(abs(i.get_points()[0][1]-self.get_centroid_origin()[1]),abs(i.get_points()[1][1]-self.get_centroid_origin()[1]))
            y_max = max(abs(i.get_points()[0][0]-self.get_centroid_origin()[0]),abs(i.get_points()[1][0]-self.get_centroid_origin()[0]))
            if z_max > z_max_distance:
                z_max_distance = z_max

            if y_max > y_max_distance:
                y_max_distance = y_max

        return (self.get_moments_of_inertia()[0]/z_max_distance, self.get_moments_of_inertia()[1]/y_max_distance)

    def return_basic_results(self):
        return [
            {
                'id':'A',
                'label': 'A',
                'label_sub': '',
                'value': round(self.get_total_area(),2),
                'unit': 'mm',
                'unit_pow': '2',
                'description': 'Total Area of Cross Section'
            },
            {
                'id':'c_y',
                'label': 'c',
                'label_sub': 'y',
                'value': round(self.get_centroid_origin()[0],2),
                'unit': 'mm',
                'unit_pow': '',
                'description': 'Centroid Position in Y'
            },
            {
                'id':'c_z',
                'label': 'c',
                'label_sub': 'z',
                'value': round(self.get_centroid_origin()[1],2),
                'unit': 'mm',
                'unit_pow': '',
                'description': 'Centroid Position in Z'
            },
            {
                'id':'I_y',
                'label': 'I',
                'label_sub': 'y',
                'value': round(self.get_moments_of_inertia()[0],2),
                'unit': 'mm',
                'unit_pow': '4',
                'description': 'Moment of Inertia around Y'
            },
            {
                'id':'I_z',
                'label': 'I',
                'label_sub': 'z',
                'value': round(self.get_moments_of_inertia()[1],2),
                'unit': 'mm',
                'unit_pow': '4',
                'description': 'Moment of Inertia around Z'
            },
            {
                'id':'W_y',
                'label': 'W',
                'label_sub': 'y',
                'value': round(self.get_section_modulus()[0],2),
                'unit': 'mm',
                'unit_pow': '3',
                'description': 'Section modulus around Y'
            },
            {
                'id':'W_z',
                'label': 'W',
                'label_sub': 'z',
                'value': round(self.get_section_modulus()[1],2),
                'unit': 'mm',
                'unit_pow': '3',
                'description': 'Section modulus around Z'
            },
        ]

class i_section(cross_section):

    def __init__(self,h,b,t_f,t_w):
        self._shapes = []
        self._shapes.append(square([-b/2,h/2],[b/2,(h/2)-t_f]))
        self._shapes.append(square([-t_w/2,(h/2)-t_f],[t_w/2,(-h/2)+t_f]))
        self._shapes.append(square([-b/2,(-h/2)+t_f],[b/2,-h/2]))

def testik(data):

    if data['type'] == "General":   # This option uses default constructor filled with shapes as arguments ------------------ Fix this so it does not have to do the fucking for loop you moron

        shapes = []

        for item in data['elements']:
            shapes.append(square([item['coordinates']['x_1'],item['coordinates']['y_1']],[item['coordinates']['x_2'],item['coordinates']['y_2']]))
        section = cross_section(shapes)

    elif data['type'] == "I-shape": # This option uses class method as alternative constructor - used For I-beams
        section = i_section(float(data['h']),float(data['b']),float(data['t_f']),float(data['t_w']))

    for item in section.return_basic_results():
        print(item)


    return section.return_basic_results()

if __name__ == '__main__':

    # Test
    item1 = square([-13,18],[-4,16])
    item2 = square([-9,16],[-8,8])
    item3 = square([-13,8],[-4,3])
    section = cross_section([item1, item2, item3])

    print('##############################################################################')

    for item in section._shapes:
        print("Points: " + str(item.get_points()))
        print('Area of item is: '+ str(item.get_area()))
        print('Centroid of item towards origin: '+ str(item.get_centroid_origin()))
        print('First Moment of Area of item towards origin: '+ str(item.get_first_moment_area()))
        print('Moment of Ineartia of item: '+ str(item.get_moment_of_inertia()))
        print('')

    print('Total Area: ' + str(section.get_total_area()))
    print('Total First Moment of Area: ' + str(section.get_first_moment_area()))
    print('Total Centroid against origin: ' + str(section.get_centroid_origin()))
    print('Total Second Moment of Area: ' + str(section.get_second_moment_area()))
    print('Total Sum Moments of Inertia: ' + str(section.get_sum_moments_of_inertia()))
    print('Total Moment of Inertia: ' + str(section.get_moments_of_inertia()))
    print('Section Modulus: ' + str(section.get_section_modulus()))

    print('##############################################################################')

    section2 = i_section(400,200,12,8)

    for item in section2._shapes:
        print("Points: " + str(item.get_points()))
        print('Area of item is: '+ str(item.get_area()))
        print('Centroid of item towards origin: '+ str(item.get_centroid_origin()))
        print('First Moment of Area of item towards origin: '+ str(item.get_first_moment_area()))
        print('Moment of Ineartia of item: '+ str(item.get_moment_of_inertia()))
        print('')

    print('Total Area: ' + str(section2.get_total_area()))
    print('Total First Moment of Area: ' + str(section2.get_first_moment_area()))
    print('Total Centroid against origin: ' + str(section2.get_centroid_origin()))
    print('Total Second Moment of Area: ' + str(section2.get_second_moment_area()))
    print('Total Sum Moments of Inertia: ' + str(section2.get_sum_moments_of_inertia()))
    print('Total Moment of Inertia: ' + str(section2.get_moments_of_inertia()))
    print('Section Modulus: ' + str(section2.get_section_modulus()))
