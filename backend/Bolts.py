import math
import pprint

Bolts = {
    'M12':{'Diameter':12},
    'M16':{'Diameter':16},
    'M20':{'Diameter':20},
    'M24':{'Diameter':24}
  }

Grades = {
    '8.8':{'R_el':355},
    '10.9':{'R_el':420},
    '12.9':{'R_el':620}
 }

def get_bolt_options():
    return [list(Bolts.keys()),list(Grades.keys())]

def distance_point_line(line_point_1, line_point_2, point):  # Calculates distance from point to line specified by 2 points. point is 2-dimensional tuple (x, y)
    distance = abs((line_point_2[1]-line_point_1[1])*point[0]-(line_point_2[0]-line_point_1[0])*point[1]+line_point_2[0]*line_point_1[1]-line_point_2[1]*line_point_1[0])/math.sqrt(math.pow(line_point_2[1]-line_point_1[1],2)+math.pow(line_point_2[0]-line_point_1[0],2))
    return distance

class boltEN:

    def __init__(self, size=None, grade=None, x=None, y=None):
        self._x = x
        self._y = y
        self._grade = grade
        self._size = size
        self._Fx_primary = None # Will get defined in Bolt pattern __init__
        self._Fy_primary = None # Will get defined in Bolt pattern __init__
        self._F_secondary = None # Will get defined in Bolt pattern __init__
        self._Fx_secondary = None # Will get defined in Bolt pattern __init__
        self._Fy_secondary = None # Will get defined in Bolt pattern __init__
        self._diameter = Bolts[size]['Diameter']
        self._quadrant = None # This specifies quadrand of bolt towards centroid - will get defined in Bolt pattern __init__
        self._bolt_angle = None # Will get defined in Bolt pattern __init__

    def get_area(self): # Update later to reflect EN1993 rules
        return (math.pi/4)*math.pow(self._diameter,2)

    def get_diameter(self):
        return self._diameter

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_Fx_primary(self):
        return self._Fx_primary

    def get_Fy_primary(self):
        return self._Fy_primary

    def get_Fx_secondary(self):
        return self._Fx_secondary

    def get_Fx_total(self):
        return self._Fx_primary + self._Fx_secondary

    def get_Fy_total(self):
        return self._Fy_primary + self._Fy_secondary

    def get_Fy_secondary(self):
        return self._Fy_secondary

    def get_F_secondary(self):
        return self._F_secondary

    def get_distance_from_centroid(self):
        return self._distance_from_centroid

    def set_Fx_primary(self,Fx_primary):
        self._Fx_primary = Fx_primary

    def set_Fy_primary(self,Fy_primary):
        self._Fy_primary = Fy_primary

    def set_F_secondary(self,F_secondary):
        self._F_secondary = F_secondary

    def set_distance_from_centroid(self,centroid):
        self._distance_from_centroid = math.sqrt(math.pow(abs(self._x-centroid[0]),2)+math.pow(abs(self._y-centroid[1]),2))

    def set_F_secondaryXY(self,centroid,moment):
        angle = math.atan(abs(self._y-centroid[1])/abs(self._x-centroid[0]))
        if self._x >= centroid[0] and self._y >= centroid[1]:
            F_x_secondary = self._F_secondary*math.sin(angle)
            F_y_secondary = -self._F_secondary*math.cos(angle)
        elif self._x >= centroid[0] and self._y < centroid[1]:
            F_x_secondary = -self._F_secondary*math.sin(angle)
            F_y_secondary = -self._F_secondary*math.cos(angle)
        elif self._x < centroid[0] and self._y <= centroid[1]:
            F_x_secondary = -self._F_secondary*math.sin(angle)
            F_y_secondary = self._F_secondary*math.cos(angle)
        else:
            F_x_secondary = self._F_secondary*math.sin(angle)
            F_y_secondary = self._F_secondary*math.cos(angle)
        self._Fx_secondary = F_x_secondary
        self._Fy_secondary = F_y_secondary

class boltPattern:

    def __init__(self, bolts, loads=None):
        self._bolts = bolts
        self._loads = loads
        self._centroid = self.get_centroid()
        self._total_moment = self.get_total_moment()
        self._total_Fx_primary = self.get_total_Fx()
        self._total_Fy_primary = self.get_total_Fy()

        for item in self._bolts:
            item.set_Fx_primary(self._total_Fx_primary/len(self._bolts))
            item.set_Fy_primary(self._total_Fy_primary/len(self._bolts))
            item.set_distance_from_centroid(self._centroid)

        self._total_square_distances = self.get_total_square_distances()

        for item in self._bolts:
            item.set_F_secondary(self._total_moment*item.get_distance_from_centroid()/self._total_square_distances)
            item.set_F_secondaryXY(self._centroid,self._total_moment)



    def get_total_square_distances(self): #This method returns sum of all bolts distances from centroid squared
        total = 0
        for item in self._bolts:
            total += math.pow(item.get_distance_from_centroid(),2)
        return total

    def get_number_bolts(self):
        return len(self._bolts)

    def get_centroid(self):
        A_total = 0
        A_x = 0
        A_y = 0

        for item in self._bolts:
            A_x += item.get_area()*item.get_x()
            A_y += item.get_area()*item.get_y()
            A_total += item.get_area()

        return A_x/A_total, A_y/A_total

    def get_total_moment(self):
        total_moment = 0
        for item in self._loads:
            moment = item.get_eq_moment(self.get_centroid())
            total_moment += moment
        return total_moment

    def get_total_Fx(self):
        total_Fx = 0
        for item in self._loads:
            try:
                total_Fx += item.get_F_x()
            except:
                pass
                #print("Get total_Fx failed (Mostly Moment appended)")
        return total_Fx

    def get_total_Fy(self):
        total_Fy = 0
        for item in self._loads:
            try:
                total_Fy += item.get_F_y()
            except:
                pass
                #print("Get total_Fy failed (Mostly Moment appended)")

        return total_Fy

    def return_results(self):
        results={
        'centroid_x':round(self.get_centroid()[0],2),
        'centroid_y':round(self.get_centroid()[1],2),
        'total_moment':round(self.get_total_moment(),2),
        'total_Fx_prim':round(self.get_total_Fx(),2),
        'total_Fy_prim':round(self.get_total_Fy(),2),


        'bolts':[]
        }

        for bolt in self._bolts:
            results['bolts'].append(
            {
                'bolt_ID': 0,
                'bolt_x': round(bolt.get_x(),2),
                'bolt_y': round(bolt.get_y(),2),
                'bolt_Fx_prim': round(bolt.get_Fx_primary(),2),
                'bolt_Fy_prim': round(bolt.get_Fy_primary(),2),
                'bolt_Fx_sec': round(bolt.get_Fx_secondary(),2),
                'bolt_Fy_sec': round(bolt.get_Fy_secondary(),2),
                'bolt_Fx_total': round(bolt.get_Fx_total(),2),
                'bolt_Fy_total': round(bolt.get_Fy_total(),2),
                'results':[
                {
                    'csdcsdcsdc':1651,
                    'sdcsdc':135131
                }

                ]
            }
            )

        return results

class Force:

    def __init__(self,x, y, angle, magnitude):  #Angle in deg
        self._x = x
        self._y = y
        self._angle = angle
        self._magnitude = magnitude

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_F(self):
        return self._magnitude

    def get_F_x(self):
        return self._magnitude*math.cos(math.radians(self._angle))

    def get_F_y(self):
        return -self._magnitude*math.sin(math.radians(self._angle))

    def get_eq_moment(self,centroid):
        point1 = (self.get_x(),self.get_y())
        point2 = (self.get_x()+self.get_F_x(),self.get_y()+self.get_F_y())
        distance = distance_point_line(point1, point2, centroid)

        if point1[0] >= centroid[0] and point1[1] >= centroid[1]:   # Force origin is in Quadrant I
            M_x_cont = self.get_F_x()*(abs(point1[1]-centroid[1]))
            M_y_cont = -self.get_F_y()*(abs(point1[0]-centroid[0]))
            print("Quadrant I")

        elif point1[0] >= centroid[0] and point1[1] < centroid[1]:   # Force origin is in Quadrant II
            M_x_cont = -self.get_F_x()*(abs(point1[1]-centroid[1]))
            M_y_cont = -self.get_F_y()*(abs(point1[0]-centroid[0]))
            print("Quadrant II")

        elif point1[0] < centroid[0] and point1[1] <= centroid[1]:   # Force origin is in Quadrant III
            M_x_cont = -self.get_F_x()*(abs(point1[1]-centroid[1]))
            M_y_cont = self.get_F_y()*(abs(point1[0]-centroid[0]))
            print("Quadrant III")

        elif point1[0] < centroid[0] and point1[1] > centroid[1]:   # Force origin is in Quadrant IV
            M_x_cont = self.get_F_x()*(abs(point1[1]-centroid[1]))
            M_y_cont = self.get_F_y()*(abs(point1[0]-centroid[0]))
            print("Quadrant IV")


        if M_x_cont+M_y_cont >= 0:
            return distance*self.get_F()
        else:
            return -distance*self.get_F()

class Moment:

    def __init__(self, magnitude):  #Angle in deg
        self._magnitude = magnitude

    def get_eq_moment(self,centroid = None):
        return self._magnitude



if __name__ == '__main__':

    bolt1 = boltEN(size='M16', grade='8.8', x=75, y=90)
    bolt2 = boltEN(size='M16', grade='8.8', x=150, y=90)
    bolt3 = boltEN(size='M16', grade='8.8', x=75, y=160)
    bolt4 = boltEN(size='M16', grade='8.8', x=150, y=160)

    force1 = Force(250,90,30,2000)
    moment1 = Moment(-22000)

    pattern = boltPattern([bolt1, bolt2, bolt3, bolt4],[force1,moment1])

    #pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(pattern.return_results())
