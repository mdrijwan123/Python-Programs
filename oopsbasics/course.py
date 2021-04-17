class Course:

    def __init__(self, name, ratings):
        self.__name = name
        self.__ratings = ratings

    def average(self):
        numberOfRatings = len(self.__ratings)
        average = sum(self.__ratings) / numberOfRatings
        print("Average Ratings For ", self.__name, " Is ", average)

    def getter(self):
        print(self.__name, self.__ratings)


c1 = Course("Java Course", [1, 2, 3, 4, 5])
c1.getter()
# print(c1.__name)
# print(c1.__ratings)
c1.average()

c2 = Course("Java Web Services", [5, 5, 5, 5])
# print(c2.__name)
# print(c2.__ratings)
c2.average()
