class Wizard(object):
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def __iadd__(self, other):
        self.rating = self.rating + len(other)
        self.age = self.age - (len(other) // 10)
        if self.age < 18:
            self.age = 18
        if self.rating > 100:
            self.rating = 100
        return self

    def change_rating(self, value):
        if self.rating + value in range(1, 101):
            if value > self.rating:
                self.age = self.age - (abs(value) // 10)
                if self.age < 18:
                    self.age = 18
            elif value < self.rating:
                self.age = self.age - (abs(value) // 10)
            self.rating += value
        else:
            if value > 100:
                self.rating = 100
            else:
                self.rating = 1
        return self

    def __call__(self, argument1):
        a = int((argument1 - self.age) * self.rating)
        return a

    def __str__(self):
        a = ("Wizard " + str(self.name) + " with " + str(self.rating) + " ratings looks " + str(self.age) + " years old")
        return a

    def __gt__(self, other):
        if self.rating > other.rating:
            return True
        elif self.rating < other.rating:
            return False
        else:
            if self.age > other.age:
                return True
            elif self.age < other.age:
                return False
            else:
                if self.name > other.name:
                    return True
                else:
                    return False

    def __lt__(self, other):
        if self.rating < other.rating:
            return True
        elif self.rating > other.rating:
            return False
        else:
            if self.age < other.age:
                return True
            elif self.age > other.age:
                return False
            else:
                if self.name < other.name:
                    return True
                else:
                    return False

    def __le__(self, other):
        if self.rating <= other.rating:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.rating >= other.rating:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.rating == other.rating:
            if self.age == other.age:
                if self.name == other.name:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        if self.rating == other.rating:
            if self.age == other.age:
                if self.name == other.name:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
