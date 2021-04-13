class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name


class ItemDiscountReport(ItemDiscount):

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_parent_data(self):
        print(f'{self.get_name()} - цена: {self.get_price()}')

    def get_info(self, price):
        print(f'{self.get_name()} - новая цена: {price}')

    def str(self):
        print(f'Цена со скидкой {self.discount} % : {int(self.get_price()) - (int(self.get_price()) * (int(self.discount) / 100))}')


item = ItemDiscountReport("Картошка", "3", "6")
item.get_parent_data()
item.str()
item.get_info("5")

