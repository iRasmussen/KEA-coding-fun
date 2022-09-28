class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'
    def about_da(self):
        return f'{self.first_name} {self.last_name} er {self.age} år gammel'
    def about_en(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'
jenr = Person('Jens', 'Rasmussen', 44)
print(jenr)
print(jenr.about_da())
print(jenr.about_en())