class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(self.name, " - цена: ", self.price)

item = ItemDiscountReport("Картошка", "3 рубля")
item.get_parent_data()



