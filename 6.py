class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


class ItemDiscountReport_First(ItemDiscount):

    def get_info(self):
        print(f'Название товара: {self.get_name()}')

class ItemDiscountReport_Second(ItemDiscount):

    def get_info(self):
        print(f'Цена товара: {self.get_price()}')



First = ItemDiscountReport_First("Картошка", "3")
First.get_info()

Second = ItemDiscountReport_Second("Картошка", "3")
Second.get_info()



