class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(self.get_name(), " - цена: ", self.get_price())

    def get_info(self, price):
        print(self.get_name(), " - цена: ", price)




item = ItemDiscountReport("Картошка", "3 рубля")
item.get_parent_data()
item.get_info("5 рублей")
