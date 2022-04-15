class Good:
    """Единица товара."""
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        if self == other:
            self.count += other.count
            return self
        else:
            print("Разные товары!")

    def __str__(self):
        return f'Товар {self.name}, цена {self.price}, количество {self.count}'


class Goods:
    """Коллекция товаров."""
    def __init__(self):
        self.value = []

    def add(self, good):
        self.value.append(good)

    def get_from_file(self, file_name):
        with open(file_name, encoding='utf-8') as data_file:
            data = data_file.readlines()
            for row in data:
                item = row.replace('\n', '').split(':')
                item_name = item[0]
                item_price = int(item[1])
                item_count = int(item[2])
                good = Good(item_name, item_price, item_count)
                self.add(good)

    def __str__(self):
        result = '\n'.join([str(x) for x in self.value])
        return result

    @staticmethod
    def static():
        print('static')

    @classmethod
    def classic(cls):
        print(cls.__name__)


# a = Good('Рыба', 250, 120)
# b = Good('Рыба', 250, 20)
# a + b

# goods = Goods()
# goods.get_from_file('C:\\Users\\fogst\\PycharmProjects\\group_2_8\\goods.txt')

# goods.static()
# goods.classic()
