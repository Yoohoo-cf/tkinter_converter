# def add(*args):
#     return sum(args)
#
# print(add(3, 4, 5, 6))
#
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#
# print(calculate(2, add=3, multiply=5))

# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")
#
# my_car = Car(make="Nissan")
# print(my_car.model)
