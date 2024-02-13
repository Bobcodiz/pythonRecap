class Channels():
    def __init__(self):
        self.channels = ["Citizen","NTV","Ramogi","Inoro","K24","KTN Home","KTN News"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

chanels = Channels()
for chanel in chanels:
    print(chanel)