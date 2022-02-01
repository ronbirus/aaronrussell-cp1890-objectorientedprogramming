#Describes the idea/concept of a house
class Address:
    def __init__(self,street, city, state, postal_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
    def to_string(self):
        return f'{self.street},{self.city},{self.postal_code},{self.country}'
class Circle:
    def __init__(self, radius:float):
        self.radius = radius
    def getarea(self):
        area = (3.14 * {self.radius}**2)
        return area
    def getcircum(self):
        circ = (2*3.14*{self.radius})
        return circ

#Create address object
my_house = Address(street="Purble Place",
                   city="St.John's",
                   state="Newfoundland",
                   postal_code="A123Y7",
                   country="Canada")
nacho_shoppe = Address(street="Newfoundland Drive",
                     city="St. John's",
                     state="Newfoundland",
                     postal_code="Unknown",
                     country="Canada")
#circles
lilcircle = Circle(radius= 3)
mediumcircle = Circle(radius=6)
bigcircle = Circle(radius=10)

print(my_house.to_string())
print(mediumcircle.getarea())
