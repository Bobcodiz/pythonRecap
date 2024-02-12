class Person:
    def __init__(self, name, age, parents, hobby):
        self.name = name
        self.age = age
        self.parents = parents
        self.hobby = hobby
        self.friends = []

    def newFriend(self):
        number = int(input("How many friends would you like to have: "))
        for _ in range(number):
            friend = input("Enter your friend: ")
            self.friends.append(friend)


# Create an instance of Person
person = Person("John", 25, ["Alice", "Bob"], "Reading")

# Call the newFriend method to add friends
person.newFriend()

# Print the person's friends
print("Your friends are:", person.friends)
print(person.name)
