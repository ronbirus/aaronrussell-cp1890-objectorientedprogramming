#Describes the idea/concept of a house
class House:
    '''
    #Attributes
    data items: adress (str). #_or_rooms(int), price(float), is_for_sale(bool)
    #Methods
    behavior: open_garage_door(), mow_lawn(), clean_up()
    '''
    def __init__(self,street_address, rooms_count, house_price, is_for_sale):
        self.address = street_address
        self.rooms = rooms_count
        self.price = house_price
        self.for_sale = is_for_sale
#My_house is an object of type House
my_house = House(street_address="1 PPD", rooms_count=10,house_price=300000,is_for_sale=True)
my_shed = House(street_address="2 PPD", rooms_count=4, house_price=10000, is_for_sale=False)


print(type(my_house))
print(my_house.price)

