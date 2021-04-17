class access_mod:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name


obj = access_mod("Rahul")
print(obj._access_mod__name)
obj.name = "Rhia"
# print(obj.__name)
print(obj.name)
