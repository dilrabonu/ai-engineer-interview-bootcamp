class Phone:
    """ Represent a phone functions"""
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = 100

    def make_call(self):
        print("Ring Ring")
    def take_photo(self):
        print("Click")

phone = Phone("Apple", "iPhone17", 1200)
phone.make_call()
phone.take_photo()
print(f"{phone.brand} {phone.model} {phone.price}")
print(f"Battery level: {phone.battery}")    

    