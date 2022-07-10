from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, product, amount):
        pass

    @abstractmethod
    def remove(self, product, amount):
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        pass

    @property
    @abstractmethod
    def get_items(self):
        return self.items

    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, product, amount):
        if (self.get_free_space - amount) >= 0:
            self.capacity -= amount
            if product in self.items:
                self.get_items[product] += amount
            else:
                self.get_items[product] = amount
        else:
            print(f"Не хватает товара на складе! Попробуй еще раз!")

    def remove(self, product, amount):
        if (self.get_free_space + amount) >= 100:
            self.capacity += amount
            if self.get_items[product] > amount:
                self.get_items[product] -= amount
            else:
                del self.get_items[product]
        else:
            print("Слишком много возврата! Верни чужое, откуда взял)")

    @property
    def get_free_space(self):
        return self.capacity

    @property
    def get_items(self):
        return self.items

    @property
    def get_unique_items_count(self):
        return len(self.items.keys())


class Shop(Store):
    def __init__(self):
        super().__init__()
        self.capacity = 20

    def add(self, product, amount):
        if (self.get_free_space - amount) >= 0 and self.get_unique_items_count < 5:
            self.capacity -= amount
            if product in self.items:
                self.get_items[product] += amount
            else:
                self.get_items[product] = amount
        else:
            print(f"Не хватает места! Попробуй еще раз!")

    def remove(self, product, amount):
        if (self.get_free_space + amount) >= 20:
            self.capacity += amount
            if self.get_items[product] > amount:
                self.get_items[product] -= amount
            else:
                del self.get_items[product]
        else:
            print("Отказано! Забираешь из магазина больше допустимого!")


class Request:
    def __init__(self, info):
        self.info = info.split()
        self.from_ = self.info[4]
        self.to = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"


def main():
    while True:
        query = input("Введите пожалуйста свой запрос:")

        if query in ["stop", "стоп"]:
            break

        request = Request(query)
        store.items = store_items
        shop.items = shop_items
        if request.to in "склад":
            if request.product in shop.items:
                if request.amount <= shop.items[request.product]:
                    print("Нужное количество товара есть в магазине!")
                else:
                    print("Нет нужного количества товара в магазине!")
                    break
            else:
                print("Такого товара нет в магазине!")
                break
            if store.get_free_space > request.amount:
                print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")
                print(f"Курьер везет {request.amount} {request.product} из {request.from_} в {request.to}")
                print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
                shop.remove(request.product, request.amount)
                store.add(request.product, request.amount)
            else:
                print("На складе не хвататет места! Попробуй уменьшить количество товара!")
                break
        elif request.to in "магазин":
            if request.product in store.items:
                if request.amount <= store.items[request.product]:
                    print("Нужное количество товара есть на складе!")
                else:
                    print("Нет нужного количества товара на складе!")
                    break
            else:
                print("Такого товара нет в магазине!")
                break
            if shop.get_free_space > request.amount and shop.get_unique_items_count <= 5:
                print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")
                print(f"Курьер везет {request.amount} {request.product} из {request.from_} в {request.to}")
                print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
                store.remove(request.product, request.amount)
                shop.add(request.product, request.amount)
            else:
                print("В магазине не хвататет места! Попробуй уменьшить количество товара!")
                break

        print(f"На складе хранится:")
        for product, amount in store.get_items.items():
            print(f"{product}: {amount}")
        print(f"В магазине хранится:")
        for product, amount in shop.get_items.items():
            print(f"{product}: {amount}")


store = Store()
shop = Shop()
store_items = {
    "печеньки": 24,
    "яблоки": 10,
    "стейк": 29,
    "молоко": 38
}
shop_items = {
    "огурцы": 2,
    "помидоры": 4,
    "бананы": 6,
    "вода": 3
}

main()
