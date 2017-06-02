squares = [x**2 for x in list(range(1, 11))]                #создаём список квадратов от 1 до 10
print(list(filter(lambda x: x in range(30,70), squares)))   #выводим квадраты от 30 до 70

###########

class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print( "Yep! I'm edible.")
        else:
            print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()




############################################
## переопределение в подклассе метода от родителся
##

class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee(1)
print(milton.full_time_wage(10))



###################

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


a = Triangle(10, 20, 60)
print(a.check_angles())

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

########################################
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point)