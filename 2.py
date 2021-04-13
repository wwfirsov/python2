class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(self.__name, " - цена: ", self.__price)

item = ItemDiscountReport("Картошка", "3 рубля")
item.get_parent_data()
