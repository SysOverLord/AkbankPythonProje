import csv
import os.path


class Pizza:
    _mult = 0
    _description = ''

    def __init__(self):
        self._description = self.__class__.__name__

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._mult


class Classic(Pizza):
    _mult = 10


class Margherita(Pizza):
    _mult = 11


class TurkPizza(Pizza):
    _mult = 12


class PlainPizza(Pizza):
    _mult = 13


class Decorator:
    _cost = 0

    def __init__(self, pizza):
        self.pizza = pizza
        self._description = self.__class__.__name__ + ' ' + self.pizza.get_description()

    def get_cost(self):
        return self._cost * self.pizza.get_cost()

    def get_description(self):
        return self._description


class Olive(Decorator):
    _cost = 1


class Mushroom(Decorator):
    _cost = 2


class GoatCheese(Decorator):
    _cost = 3


class Meat(Decorator):
    _cost = 4


class Onion(Decorator):
    _cost = 5


class Corn(Decorator):
    _cost = 6


_enumSauce = [Olive, Mushroom, GoatCheese, Meat, Onion, Corn]
_enumPizza = [Classic, Margherita, TurkPizza, PlainPizza]


def readMenu():
    menuFile = open("Menu.txt", "r")
    menuStr = menuFile.read()
    return menuStr


def createOrdersDatabase():
    fields = ['Name', 'TC', 'Card Number', 'Card Password', 'Cost']
    saveTransaction(fields)


def saveTransaction(transactionInfo):
    with open(r'Orders_Database.csv', 'a',newline='') as file:
        fWriter = csv.writer(file)
        fWriter.writerow(transactionInfo)
        file.close()


def main():
    if os.path.isfile('Orders_Database.csv') is False:
        createOrdersDatabase()

    print(readMenu())
    selectedPizza = None
    selectedSauce = None
    while 1 == 1:
        selection = int(input("Please select from menu: "))
        if selection == 0:
            break

        if selection <= 4:
            selectedPizza = _enumPizza[selection - 1]()
            print('Selected Pizza: ', selectedPizza.get_description())
            if selectedSauce is not None:
                selectedSauce.pizza = selectedPizza
        elif 4 < selection < 11 or selection > 16:
            print('Invalid input.')
        elif selectedPizza is None:
            print("a pizza must be selected before adding sauces. ")
            continue
        else:
            # Instance initate
            selectedSauce = _enumSauce[selection - 11](selectedPizza)
            print('Selected Sauce: ', selectedSauce.__class__.__name__)
            break

    print('Total: ', selectedSauce.get_cost())
    print('Description: ', selectedSauce.get_description())

    mName = input('Enter name: ')
    mId = input('Enter id number: ')
    while len(mId) != 11:
        mId = input('Please enter id number again it must be 11 characters long: ')

    mCC = input('Enter credit card number: ')
    while len(mCC) != 16:
        mCC = input('Please enter credit card number again it must be 16 numbers long: ')
    mCCP = input('Enter credit card password: ')
    saveTransaction([mName, mId, mCC, mCCP, selectedPizza.get_cost()])


if __name__ == '__main__':
    main()
