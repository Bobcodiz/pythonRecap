class Persona:
    def __init__(self):
        self.persona = {"name": "John", "age": 30, "city": "New York", "email": "john@gmail"}
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.persona):
            raise StopIteration

        return self.persona


persona = Persona()
for person in persona:
    print(person)
