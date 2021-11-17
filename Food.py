import requests
class Drink():
	def __init__(self, id,name, description, price):
		self.type = "Drink"
		self.name = name
		self.id = id
		self.description = description
		self.price = price

class Pizza():
	def __init__(self, id, name, description, price):
		self.type = "Pizza"
		self.name = name
		self.id = id
		self.description = description
		self.price = price

class Dessert():
	def __init__(self, id, name, description, price):
		self.type = "Deesert"
		self.id = id
		self.name = name
		self.description = description
		self.price = price

def create_drinks():
	power_green =  Drink(1, "Power Green - Healty and energy drink", 16)
	cola_zero =  Drink(2, "Cola Zero- ", 12)
	cola =  Drink(3, "Cola-", 12)
	sprite_zero =  Drink(4, "Sprite zero-", 12)
	sprite =  Drink(5, "Sprite-", 12)
	soda =  Drink(6, "Soda description", 10)
	water =  Drink(7, "Water description", 10)
	return {1:power_green, 2:cola_zero, 3:cola, 4:sprite_zero, 5:sprite, 6:soda, 7:water}

def create_pizza():
	margratia = Pizza(1, "Margraite", 50)
	pongi = Pizza(2, "pongi", 55)
	calbaria = Pizza(3, "Calabria", 55)
	orogola = Pizza(4, "Orogola", 55)
	return {1:margratia, 2:pongi, 3:calbaria, 4:orogola}


def create_dessert():
	termiso = Dessert(1,"Termiso", 29)
	chessecake = Dessert(2,"Chessecake", 29)
	tarat = Dessert(3,"Tarat", 27)
	return {1:termiso, 2:chessecake, 3:tarat}

def print_food_by_type(drinks):
	s =  "Drinks:\r\n"
	for drink in drinks.keys():
		s += print_specific_item(drinks[drink])
	return s
def print_specific_item(drink):
	s = ""
	s += "id = " + str(drink.id) + ", description = " + drink.description + ", price = " + str(drink.price) + "\r\n"
	return s

def getMenu():
	menu = {}
	menu["drink"] = {}
	menu["pizza"] = {}
	menu["dessert"] = {}
	url = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
	params = dict(culture='en',uiCulture='en',restaurantId=19156,deliveryMethod='pickup')
	data = requests.get(url=url, params=params).json()
	for category in range(len(data['Data']['categoriesList'])):		
		categ = data['Data']['categoriesList'][category]['categoryName']
		if categ == "Pizzas":
			pizzaz_list = data['Data']['categoriesList'][category]['dishList']
			for pizza in pizzaz_list:
				#print(int(pizza['dishId']))
				menu["pizza"][int(pizza['dishId'])] = Pizza(int(pizza['dishId']), pizza['dishName'],pizza['dishDescription'],pizza['dishPrice'])
		if categ == "Drinks":
			drink_lst = data['Data']['categoriesList'][category]['dishList']
			for drink in drink_lst:
				print(int(drink['dishId']))
				menu["drink"][int(drink['dishId'])] = Drink(int(drink['dishId']), drink['dishName'],drink['dishDescription'],drink['dishPrice'])
		if categ == "Desserts":
			dessert_list = data['Data']['categoriesList'][category]['dishList']
			for dessert in dessert_list:
				#print(int(dessert['dishId']))
				menu["dessert"][int(dessert['dishId'])] = Dessert(int(dessert['dishId']), dessert['dishName'],dessert['dishDescription'],dessert['dishPrice'])

	return menu
