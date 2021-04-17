class room:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name)
        print(self.marks)
        self.print_display()

    @staticmethod
    def print_display():
        i = 0
        print("Hello,{}".format(i))
        i += 1


rm = room("Aryan", 89)
rm.display()
room.print_display()
km = room("Ashok",87)
km.display()
room.print_display()